from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        best = float("inf")

        for right, num in enumerate(nums):
            current_sum += num

            while current_sum >= target:
                best = min(best, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if best == float("inf") else best
