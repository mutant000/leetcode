class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hexadecimal_digits = "0123456789abcdef"
        num &= 0xFFFFFFFF
        reversed_result = []

        while num:
            reversed_result.append(hexadecimal_digits[num & 15])
            num >>= 4

        return "".join(reversed(reversed_result))
