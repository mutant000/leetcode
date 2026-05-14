from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path.copy())
                return

            for index in range(start, len(candidates)):
                candidate = candidates[index]
                if candidate > remaining:
                    break

                path.append(candidate)
                backtrack(index, remaining - candidate)
                path.pop()

        backtrack(0, target)
        return result
