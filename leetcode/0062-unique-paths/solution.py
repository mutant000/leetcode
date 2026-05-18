class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for column in range(1, n):
                dp[column] += dp[column - 1]

        return dp[-1]
