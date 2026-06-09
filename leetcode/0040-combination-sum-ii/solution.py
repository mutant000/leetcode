from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index - 1]:
                    continue

                if candidates[index] > remaining:
                    break

                path.append(candidates[index])
                backtrack(index + 1, remaining - candidates[index])
                path.pop()

        backtrack(0, target)
        return result
