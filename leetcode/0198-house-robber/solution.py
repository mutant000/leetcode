from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        best_without_previous = 0
        best_with_or_without_previous = 0

        for money in nums:
            best_without_previous, best_with_or_without_previous = (
                best_with_or_without_previous,
                max(best_with_or_without_previous, best_without_previous + money),
            )

        return best_with_or_without_previous
