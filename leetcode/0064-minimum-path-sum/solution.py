from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        dp = [0] * columns
        dp[0] = grid[0][0]

        for column in range(1, columns):
            dp[column] = dp[column - 1] + grid[0][column]

        for row in range(1, rows):
            dp[0] += grid[row][0]
            for column in range(1, columns):
                dp[column] = min(dp[column], dp[column - 1]) + grid[row][column]

        return dp[-1]
