class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        if dividend == int_min and divisor == -1:
            return int_max

        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

        while dividend >= divisor:
            current = divisor
            multiple = 1

            while dividend >= (current << 1):
                current <<= 1
                multiple <<= 1

            dividend -= current
            quotient += multiple

        if negative:
            quotient = -quotient

        return max(int_min, min(int_max, quotient))
