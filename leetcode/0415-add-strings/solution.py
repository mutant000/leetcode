class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        first_index = len(num1) - 1
        second_index = len(num2) - 1
        carry = 0
        reversed_digits = []

        while first_index >= 0 or second_index >= 0 or carry:
            first_digit = 0
            second_digit = 0

            if first_index >= 0:
                first_digit = ord(num1[first_index]) - ord("0")
                first_index -= 1
            if second_index >= 0:
                second_digit = ord(num2[second_index]) - ord("0")
                second_index -= 1

            digit_sum = first_digit + second_digit + carry
            reversed_digits.append(str(digit_sum % 10))
            carry = digit_sum // 10

        return "".join(reversed(reversed_digits))
