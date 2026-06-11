from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []

        def backtrack(start: int) -> None:
            result.append(path[:])

            for index in range(start, len(nums)):
                if index > start and nums[index] == nums[index - 1]:
                    continue

                path.append(nums[index])
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return result
