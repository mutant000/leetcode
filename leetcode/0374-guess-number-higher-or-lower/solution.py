# The guess API is already defined for you.
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            if result < 0:
                right = mid - 1
            else:
                left = mid + 1

        return -1
