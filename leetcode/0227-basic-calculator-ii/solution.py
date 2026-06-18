class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        sign = "+"

        for index, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)

            if char in "+-*/" or index == len(s) - 1:
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    stack.append(stack.pop() * number)
                else:
                    previous = stack.pop()
                    if previous < 0:
                        stack.append(-((-previous) // number))
                    else:
                        stack.append(previous // number)

                sign = char
                number = 0

        return sum(stack)
