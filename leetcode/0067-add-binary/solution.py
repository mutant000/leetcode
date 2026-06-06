class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index_a = len(a) - 1
        index_b = len(b) - 1
        carry = 0
        result = []

        while index_a >= 0 or index_b >= 0 or carry:
            digit_a = int(a[index_a]) if index_a >= 0 else 0
            digit_b = int(b[index_b]) if index_b >= 0 else 0

            total = digit_a + digit_b + carry
            result.append(str(total % 2))
            carry = total // 2

            index_a -= 1
            index_b -= 1

        return "".join(reversed(result))
