from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total_slices = 0
        slices_ending_here = 0

        for index in range(2, len(nums)):
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]:
                slices_ending_here += 1
                total_slices += slices_ending_here
            else:
                slices_ending_here = 0

        return total_slices
