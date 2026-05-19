from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        last_index = len(nums) - 1

        for index, jump in enumerate(nums):
            if index > farthest:
                return False

            farthest = max(farthest, index + jump)
            if farthest >= last_index:
                return True

        return True
