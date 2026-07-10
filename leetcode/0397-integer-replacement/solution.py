class Solution:
    def integerReplacement(self, n: int) -> int:
        operation_count = 0

        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
            operation_count += 1

        return operation_count
