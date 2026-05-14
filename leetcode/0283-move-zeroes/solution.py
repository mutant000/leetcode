from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0

        for num in nums:
            if num != 0:
                nums[write] = num
                write += 1

        for index in range(write, len(nums)):
            nums[index] = 0
