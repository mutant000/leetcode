import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        max_heap = []
        index = 0

        for _ in range(k):
            while index < len(projects) and projects[index][0] <= w:
                heapq.heappush(max_heap, -projects[index][1])
                index += 1

            if not max_heap:
                break

            w -= heapq.heappop(max_heap)

        return w
