from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                result.append(path[:])
                return

            need = k - len(path)
            for value in range(start, n - need + 2):
                path.append(value)
                backtrack(value + 1)
                path.pop()

        backtrack(1)
        return result
