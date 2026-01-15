import random
from typing import List


class RandomStrategy:
    def __init__(self, rng: random.Random = None):
        self._rng = rng or random.Random()

    def find_card(self, prisoner: int, drawers: List[int], max_attempts: int) -> bool:
        n = len(drawers)
        choices = self._rng.sample(range(n), min(max_attempts, n))
        for idx in choices:
            if drawers[idx] == prisoner:
                return True
        return False
