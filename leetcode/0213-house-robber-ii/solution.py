from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(houses: List[int]) -> int:
            prev_two = 0
            prev_one = 0

            for money in houses:
                prev_two, prev_one = prev_one, max(prev_one, prev_two + money)

            return prev_one

        if len(nums) == 1:
            return nums[0]

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
