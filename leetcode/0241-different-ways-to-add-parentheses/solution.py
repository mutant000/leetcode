from functools import lru_cache
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def compute(left: int, right: int) -> tuple[int, ...]:
            values = []

            for index in range(left, right):
                operator = expression[index]
                if operator not in "+-*":
                    continue

                left_values = compute(left, index)
                right_values = compute(index + 1, right)

                for left_value in left_values:
                    for right_value in right_values:
                        if operator == "+":
                            values.append(left_value + right_value)
                        elif operator == "-":
                            values.append(left_value - right_value)
                        else:
                            values.append(left_value * right_value)

            if not values:
                values.append(int(expression[left:right]))

            return tuple(values)

        return list(compute(0, len(expression)))
