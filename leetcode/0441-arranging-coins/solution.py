class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        answer = 0

        while left <= right:
            rows = (left + right) // 2
            required = rows * (rows + 1) // 2

            if required <= n:
                answer = rows
                left = rows + 1
            else:
                right = rows - 1

        return answer
