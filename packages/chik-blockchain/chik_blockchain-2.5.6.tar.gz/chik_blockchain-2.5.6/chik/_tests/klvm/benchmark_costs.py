from __future__ import annotations

from chik_rs import SpendBundle
from chik_rs.sized_ints import uint64

from chik._tests.util.get_name_puzzle_conditions import get_name_puzzle_conditions
from chik.consensus.cost_calculator import NPCResult
from chik.consensus.default_constants import DEFAULT_CONSTANTS
from chik.full_node.bundle_tools import simple_solution_generator
from chik.types.blockchain_format.program import INFINITE_COST
from chik.types.generator_types import BlockGenerator


def cost_of_spend_bundle(spend_bundle: SpendBundle) -> int:
    program: BlockGenerator = simple_solution_generator(spend_bundle)
    # always use the post soft-fork2 semantics
    npc_result: NPCResult = get_name_puzzle_conditions(
        program,
        INFINITE_COST,
        mempool_mode=True,
        height=DEFAULT_CONSTANTS.HARD_FORK_HEIGHT,
        constants=DEFAULT_CONSTANTS,
    )
    return uint64(0 if npc_result.conds is None else npc_result.conds.cost)
