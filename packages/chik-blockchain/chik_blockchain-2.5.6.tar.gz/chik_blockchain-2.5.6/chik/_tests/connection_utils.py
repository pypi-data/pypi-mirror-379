from __future__ import annotations

import asyncio
import logging
from pathlib import Path

import aiohttp
from chik_rs.sized_bytes import bytes32
from chik_rs.sized_ints import uint16
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization

from chik._tests.util.time_out_assert import time_out_assert
from chik.apis import ApiProtocolRegistry
from chik.protocols.outbound_message import NodeType
from chik.protocols.shared_protocol import default_capabilities
from chik.server.server import ChikServer, ssl_context_for_client
from chik.server.ssl_context import chik_ssl_ca_paths, private_ssl_ca_paths
from chik.server.ws_connection import WSChikConnection
from chik.ssl.create_ssl import generate_ca_signed_cert
from chik.types.peer_info import PeerInfo
from chik.util.config import load_config
from chik.util.timing import adjusted_timeout

log = logging.getLogger(__name__)


async def disconnect_all(server: ChikServer) -> None:
    connections = list(server.all_connections.values())
    await asyncio.gather(*(connection.close() for connection in connections))

    await asyncio.sleep(adjusted_timeout(5))  # 5 seconds to allow connections and tasks to all drain


async def disconnect_all_and_reconnect(server: ChikServer, reconnect_to: ChikServer, self_hostname: str) -> bool:
    await disconnect_all(server)
    return await server.start_client(PeerInfo(self_hostname, uint16(reconnect_to.get_port())), None)


async def add_dummy_connection(
    server: ChikServer,
    self_hostname: str,
    dummy_port: int,
    type: NodeType = NodeType.FULL_NODE,
    *,
    additional_capabilities: list[tuple[uint16, str]] = [],
) -> tuple[asyncio.Queue, bytes32]:
    wsc, peer_id = await add_dummy_connection_wsc(
        server, self_hostname, dummy_port, type, additional_capabilities=additional_capabilities
    )

    return wsc.incoming_queue, peer_id


async def add_dummy_connection_wsc(
    server: ChikServer,
    self_hostname: str,
    dummy_port: int,
    type: NodeType = NodeType.FULL_NODE,
    additional_capabilities: list[tuple[uint16, str]] = [],
) -> tuple[WSChikConnection, bytes32]:
    timeout = aiohttp.ClientTimeout(total=10)
    session = aiohttp.ClientSession(timeout=timeout)
    config = load_config(server.root_path, "config.yaml")

    ca_crt_path: Path
    ca_key_path: Path
    authenticated_client_types: set[NodeType] = {NodeType.HARVESTER}
    if type in authenticated_client_types:
        private_ca_crt_path, private_ca_key_path = private_ssl_ca_paths(server.root_path, config)
        ca_crt_path = private_ca_crt_path
        ca_key_path = private_ca_key_path
    else:
        chik_ca_crt_path, chik_ca_key_path = chik_ssl_ca_paths(server.root_path, config)
        ca_crt_path = chik_ca_crt_path
        ca_key_path = chik_ca_key_path

    dummy_crt_path = server.root_path / "dummy.crt"
    dummy_key_path = server.root_path / "dummy.key"
    generate_ca_signed_cert(ca_crt_path.read_bytes(), ca_key_path.read_bytes(), dummy_crt_path, dummy_key_path)
    ssl_context = ssl_context_for_client(ca_crt_path, ca_key_path, dummy_crt_path, dummy_key_path)
    pem_cert = x509.load_pem_x509_certificate(dummy_crt_path.read_bytes(), default_backend())
    der_cert = x509.load_der_x509_certificate(pem_cert.public_bytes(serialization.Encoding.DER), default_backend())
    peer_id = bytes32(der_cert.fingerprint(hashes.SHA256()))
    url = f"wss://{self_hostname}:{server._port}/ws"
    ws = await session.ws_connect(url, autoclose=True, autoping=True, ssl=ssl_context)
    wsc = WSChikConnection.create(
        type,
        ws,
        server.api,
        dummy_port,
        log,
        True,
        server.received_message_callback,
        None,
        peer_id,
        100,
        30,
        local_capabilities_for_handshake=default_capabilities[type] + additional_capabilities,
        class_for_type=ApiProtocolRegistry,
    )
    await wsc.perform_handshake(server._network_id, dummy_port, type)
    if wsc.incoming_message_task is not None:
        wsc.incoming_message_task.cancel()
    return wsc, peer_id


async def connect_and_get_peer(server_1: ChikServer, server_2: ChikServer, self_hostname: str) -> WSChikConnection:
    """
    Connect server_2 to server_1, and get return the connection in server_1.
    """
    await server_2.start_client(PeerInfo(self_hostname, server_1.get_port()))

    async def connected():
        for node_id_c, _ in server_1.all_connections.items():
            if node_id_c == server_2.node_id:
                return True
        return False

    await time_out_assert(10, connected, True)
    for node_id, wsc in server_1.all_connections.items():
        if node_id == server_2.node_id:
            return wsc
    assert False
