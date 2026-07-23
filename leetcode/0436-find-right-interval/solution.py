from bisect import bisect_left
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted(
            (interval[0], index) for index, interval in enumerate(intervals)
        )
        start_values = [start for start, _ in starts]
        result = []

        for _, end in intervals:
            position = bisect_left(start_values, end)

            if position == len(starts):
                result.append(-1)
            else:
                result.append(starts[position][1])

        return result
