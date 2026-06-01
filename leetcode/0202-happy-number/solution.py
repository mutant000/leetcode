class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.next_number(n)

        return n == 1

    def next_number(self, n: int) -> int:
        total = 0

        while n:
            n, digit = divmod(n, 10)
            total += digit * digit

        return total
