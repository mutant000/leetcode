from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for index, value in enumerate(nums):
                if used[index]:
                    continue

                used[index] = True
                path.append(value)
                backtrack()
                path.pop()
                used[index] = False

        backtrack()
        return result
