from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        values = [1]

        for num in nums:
            if num > 0:
                values.append(num)

        values.append(1)
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for width in range(2, n):
            for left in range(0, n - width):
                right = left + width

                for last in range(left + 1, right):
                    coins = values[left] * values[last] * values[right]
                    coins += dp[left][last] + dp[last][right]
                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]
