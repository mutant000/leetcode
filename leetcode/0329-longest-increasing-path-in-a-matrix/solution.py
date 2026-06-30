from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        @lru_cache(None)
        def dfs(row: int, col: int) -> int:
            best = 1
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and matrix[next_row][next_col] > matrix[row][col]
                ):
                    best = max(best, 1 + dfs(next_row, next_col))
            return best

        return max(dfs(row, col) for row in range(rows) for col in range(cols))
