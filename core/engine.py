import random
from typing import List, Optional
from .model import generate_permutation
from .types import Strategy


def run_trial(
    strategy: Strategy,
    n: int = 100,
    k: int = 50,
    rng: Optional[random.Random] = None
) -> bool:
    """
    단일 시행: n명의 죄수가 모두 성공하면 True
    """
    drawers = generate_permutation(n, rng)
    for prisoner in range(1, n + 1):
        if not strategy.find_card(prisoner, drawers, k):
            return False
    return True


def simulate(
    strategy: Strategy,
    trials: int,
    n: int = 100,
    k: int = 50,
    seed: Optional[int] = None
) -> int:
    """
    여러 번 시행하여 전원 성공 횟수 반환
    """
    rng = random.Random(seed)
    wins = 0
    for _ in range(trials):
        if run_trial(strategy, n, k, rng):
            wins += 1
    return wins
