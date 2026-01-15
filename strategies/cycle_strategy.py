from typing import List


class CycleStrategy:
    def find_card(self, prisoner: int, drawers: List[int], max_attempts: int) -> bool:
        current = prisoner
        for _ in range(max_attempts):
            card = drawers[current - 1]  # 1-indexed to 0-indexed
            if card == prisoner:
                return True
            current = card
        return False
