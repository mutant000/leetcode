from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cols = len(matrix[0])
        dp = [0] * (cols + 1)
        max_side = 0

        for row in matrix:
            previous_diagonal = 0

            for col in range(1, cols + 1):
                temp = dp[col]

                if row[col - 1] == "1":
                    dp[col] = min(dp[col], dp[col - 1], previous_diagonal) + 1
                    max_side = max(max_side, dp[col])
                else:
                    dp[col] = 0

                previous_diagonal = temp

        return max_side * max_side
