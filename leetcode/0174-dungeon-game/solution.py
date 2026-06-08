from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [float("inf")] * (cols + 1)
        dp[cols - 1] = 1

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                need = min(dp[col], dp[col + 1]) - dungeon[row][col]
                dp[col] = max(1, need)

        return dp[0]
