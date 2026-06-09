class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0

        while x:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        reversed_num *= sign
        if reversed_num < -(1 << 31) or reversed_num > (1 << 31) - 1:
            return 0

        return reversed_num
