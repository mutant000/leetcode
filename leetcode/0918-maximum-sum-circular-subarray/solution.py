from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        max_ending = nums[0]
        max_sum = nums[0]
        min_ending = nums[0]
        min_sum = nums[0]

        for num in nums[1:]:
            max_ending = max(num, max_ending + num)
            max_sum = max(max_sum, max_ending)

            min_ending = min(num, min_ending + num)
            min_sum = min(min_sum, min_ending)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)
