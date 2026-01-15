from typing import Protocol, List


class Strategy(Protocol):
    def find_card(self, prisoner: int, drawers: List[int], max_attempts: int) -> bool:
        """
        prisoner: 죄수 번호 (1-indexed)
        drawers: drawers[i] = i+1번 서랍에 들어있는 카드 번호
        max_attempts: 최대 열 수 있는 서랍 수
        Returns: 자기 번호 카드를 찾았는지 여부
        """
        ...
