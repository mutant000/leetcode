from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        removed = 0
        current_end = float("-inf")

        for start, end in intervals:
            if start < current_end:
                removed += 1
            else:
                current_end = end

        return removed
