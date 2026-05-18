class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        base = 1
        while base * base <= n:
            squares.append(base * base)
            base += 1

        dp = [0] + [n] * n
        for value in range(1, n + 1):
            for square in squares:
                if square > value:
                    break
                dp[value] = min(dp[value], dp[value - square] + 1)

        return dp[n]
