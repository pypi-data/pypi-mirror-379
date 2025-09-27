from __future__ import annotations

from dataclasses import dataclass

from chik_rs import CoinSpend
from chik_rs.sized_bytes import bytes32
from chik_rs.sized_ints import uint64

from chik.types.blockchain_format.coin import Coin as _Coin
from chik.types.blockchain_format.program import Program
from chik.util.streamable import Streamable
from chik.wallet.util.klvm_streamable import klvm_streamable

# This file contains the base types for communication between a wallet and an offline transaction signer.
# These types should be compliant with CHIP-0028


@klvm_streamable
@dataclass(frozen=True)
class Coin(Streamable):
    parent_coin_id: bytes32
    puzzle_hash: bytes32
    amount: uint64


@klvm_streamable
@dataclass(frozen=True)
class Spend(Streamable):
    coin: Coin
    puzzle: Program
    solution: Program

    @classmethod
    def from_coin_spend(cls, coin_spend: CoinSpend) -> Spend:
        return cls(
            Coin(
                coin_spend.coin.parent_coin_info,
                coin_spend.coin.puzzle_hash,
                uint64(coin_spend.coin.amount),
            ),
            Program.from_serialized(coin_spend.puzzle_reveal),
            Program.from_serialized(coin_spend.solution),
        )

    def as_coin_spend(self) -> CoinSpend:
        return CoinSpend(
            _Coin(
                self.coin.parent_coin_id,
                self.coin.puzzle_hash,
                self.coin.amount,
            ),
            self.puzzle.to_serialized(),
            self.solution.to_serialized(),
        )


@klvm_streamable
@dataclass(frozen=True)
class TransactionInfo(Streamable):
    spends: list[Spend]


@klvm_streamable
@dataclass(frozen=True)
class SigningTarget(Streamable):
    fingerprint: bytes
    message: bytes
    hook: bytes32


@klvm_streamable
@dataclass(frozen=True)
class SumHint(Streamable):
    fingerprints: list[bytes]
    synthetic_offset: bytes
    final_pubkey: bytes


@klvm_streamable
@dataclass(frozen=True)
class PathHint(Streamable):
    root_fingerprint: bytes
    path: list[uint64]


@klvm_streamable
@dataclass(frozen=True)
class KeyHints(Streamable):
    sum_hints: list[SumHint]
    path_hints: list[PathHint]


@klvm_streamable
@dataclass(frozen=True)
class SigningInstructions(Streamable):
    key_hints: KeyHints
    targets: list[SigningTarget]


@klvm_streamable
@dataclass(frozen=True)
class UnsignedTransaction(Streamable):
    transaction_info: TransactionInfo
    signing_instructions: SigningInstructions


@klvm_streamable
@dataclass(frozen=True)
class SigningResponse(Streamable):
    signature: bytes
    hook: bytes32


@klvm_streamable
@dataclass(frozen=True)
class Signature(Streamable):
    type: str
    signature: bytes


@klvm_streamable
@dataclass(frozen=True)
class SignedTransaction(Streamable):
    transaction_info: TransactionInfo
    signatures: list[Signature]
