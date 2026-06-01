class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        number = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char in "+-":
                result += sign * number
                number = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * number
                number = 0
                previous_sign = stack.pop()
                previous_result = stack.pop()
                result = previous_result + previous_sign * result

        return result + sign * number
