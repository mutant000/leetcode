class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(2, n + 1):
            for left in range(1, n - length + 2):
                right = left + length - 1
                dp[left][right] = min(
                    guess + max(dp[left][guess - 1], dp[guess + 1][right])
                    for guess in range(left, right + 1)
                )

        return dp[1][n]
