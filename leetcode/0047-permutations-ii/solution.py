from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)
        result = []
        path = []

        def backtrack() -> None:
            if len(path) == len(nums):
                result.append(path[:])
                return

            for index in range(len(nums)):
                if used[index]:
                    continue

                if index > 0 and nums[index] == nums[index - 1] and not used[index - 1]:
                    continue

                used[index] = True
                path.append(nums[index])
                backtrack()
                path.pop()
                used[index] = False

        backtrack()
        return result
