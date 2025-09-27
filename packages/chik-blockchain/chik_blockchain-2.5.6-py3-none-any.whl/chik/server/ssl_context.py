from __future__ import annotations

from pathlib import Path
from typing import Any


def public_ssl_paths(path: Path, config: dict[str, Any]) -> tuple[Path, Path]:
    return (
        path / config["ssl"]["public_crt"],
        path / config["ssl"]["public_key"],
    )


def private_ssl_paths(path: Path, config: dict[str, Any]) -> tuple[Path, Path]:
    return (
        path / config["ssl"]["private_crt"],
        path / config["ssl"]["private_key"],
    )


def private_ssl_ca_paths(path: Path, config: dict[str, Any]) -> tuple[Path, Path]:
    return (
        path / config["private_ssl_ca"]["crt"],
        path / config["private_ssl_ca"]["key"],
    )


def chik_ssl_ca_paths(path: Path, config: dict[str, Any]) -> tuple[Path, Path]:
    return (
        path / config["chik_ssl_ca"]["crt"],
        path / config["chik_ssl_ca"]["key"],
    )
