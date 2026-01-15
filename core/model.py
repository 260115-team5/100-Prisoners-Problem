import random
from typing import List, Optional


def generate_permutation(n: int, rng: Optional[random.Random] = None) -> List[int]:
    """
    1~n 카드를 무작위로 섞어 서랍 배치 생성
    drawers[i] = i+1번 서랍에 들어있는 카드 번호
    """
    if rng is None:
        rng = random.Random()
    cards = list(range(1, n + 1))
    rng.shuffle(cards)
    return cards
