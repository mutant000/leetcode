from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []

        def backtrack(start: int) -> None:
            result.append(path.copy())

            for index in range(start, len(nums)):
                path.append(nums[index])
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return result
