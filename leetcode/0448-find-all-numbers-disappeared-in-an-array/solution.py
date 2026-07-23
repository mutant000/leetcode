from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for value in nums:
            index = abs(value) - 1
            nums[index] = -abs(nums[index])

        return [
            index + 1
            for index, value in enumerate(nums)
            if value > 0
        ]
