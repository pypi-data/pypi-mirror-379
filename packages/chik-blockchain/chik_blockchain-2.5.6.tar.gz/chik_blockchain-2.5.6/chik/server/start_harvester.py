from __future__ import annotations

import os
import pathlib
import sys
from typing import Any, Optional

from chik_rs import ConsensusConstants

from chik.apis import ApiProtocolRegistry
from chik.consensus.constants import replace_str_to_bytes
from chik.consensus.default_constants import DEFAULT_CONSTANTS, update_testnet_overrides
from chik.harvester.harvester import Harvester
from chik.harvester.harvester_api import HarvesterAPI
from chik.harvester.harvester_rpc_api import HarvesterRpcApi
from chik.protocols.outbound_message import NodeType
from chik.server.aliases import HarvesterService
from chik.server.resolve_peer_info import get_unresolved_peer_infos
from chik.server.signal_handlers import SignalHandlers
from chik.server.start_service import RpcInfo, Service, async_run
from chik.types.peer_info import UnresolvedPeerInfo
from chik.util.chik_logging import initialize_service_logging
from chik.util.config import load_config, load_config_cli
from chik.util.default_root import resolve_root_path
from chik.util.task_timing import maybe_manage_task_instrumentation

# See: https://bugs.python.org/issue29288
"".encode("idna")

SERVICE_NAME = "harvester"


def create_harvester_service(
    root_path: pathlib.Path,
    config: dict[str, Any],
    consensus_constants: ConsensusConstants,
    farmer_peers: set[UnresolvedPeerInfo],
    connect_to_daemon: bool = True,
) -> HarvesterService:
    service_config = config[SERVICE_NAME]

    network_id = service_config["selected_network"]
    overrides = service_config["network_overrides"]["constants"][network_id]
    update_testnet_overrides(network_id, overrides)
    updated_constants = replace_str_to_bytes(consensus_constants, **overrides)

    node = Harvester(root_path, service_config, updated_constants)
    peer_api = HarvesterAPI(node)
    network_id = service_config["selected_network"]

    rpc_info: Optional[RpcInfo[HarvesterRpcApi]] = None
    if service_config.get("start_rpc_server", True):
        rpc_info = (HarvesterRpcApi, service_config["rpc_port"])

    return Service(
        root_path=root_path,
        config=config,
        node=node,
        peer_api=peer_api,
        node_type=NodeType.HARVESTER,
        advertised_port=None,
        service_name=SERVICE_NAME,
        connect_peers=farmer_peers,
        network_id=network_id,
        rpc_info=rpc_info,
        connect_to_daemon=connect_to_daemon,
        class_for_type=ApiProtocolRegistry,
    )


async def async_main(root_path: pathlib.Path) -> int:
    # TODO: refactor to avoid the double load
    config = load_config(root_path, "config.yaml")
    service_config = load_config_cli(root_path, "config.yaml", SERVICE_NAME)
    config[SERVICE_NAME] = service_config
    initialize_service_logging(service_name=SERVICE_NAME, config=config, root_path=root_path)
    farmer_peers = get_unresolved_peer_infos(service_config, NodeType.FARMER)

    service = create_harvester_service(root_path, config, DEFAULT_CONSTANTS, farmer_peers)
    async with SignalHandlers.manage() as signal_handlers:
        await service.setup_process_global_state(signal_handlers=signal_handlers)
        await service.run()

    return 0


def main() -> int:
    root_path = resolve_root_path(override=None)

    with maybe_manage_task_instrumentation(
        enable=os.environ.get(f"CHIK_INSTRUMENT_{SERVICE_NAME.upper()}") is not None
    ):
        return async_run(coro=async_main(root_path=root_path))


if __name__ == "__main__":
    sys.exit(main())
