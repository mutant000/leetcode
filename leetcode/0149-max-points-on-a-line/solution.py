from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        answer = 2

        for index, (x1, y1) in enumerate(points):
            slopes = defaultdict(int)

            for x2, y2 in points[index + 1:]:
                delta_x = x2 - x1
                delta_y = y2 - y1

                if delta_x == 0:
                    slope = (0, 1)
                elif delta_y == 0:
                    slope = (1, 0)
                else:
                    divisor = gcd(delta_x, delta_y)
                    delta_x //= divisor
                    delta_y //= divisor

                    if delta_x < 0:
                        delta_x = -delta_x
                        delta_y = -delta_y

                    slope = (delta_x, delta_y)

                slopes[slope] += 1
                answer = max(answer, slopes[slope] + 1)

        return answer
