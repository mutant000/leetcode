from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for index in range(n):
            while 1 <= nums[index] <= n and nums[nums[index] - 1] != nums[index]:
                target_index = nums[index] - 1
                nums[index], nums[target_index] = nums[target_index], nums[index]

        for index, num in enumerate(nums):
            if num != index + 1:
                return index + 1

        return n + 1
