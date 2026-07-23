from collections import defaultdict
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0

        for center_x, center_y in points:
            distance_counts = defaultdict(int)

            for point_x, point_y in points:
                difference_x = center_x - point_x
                difference_y = center_y - point_y
                distance = difference_x**2 + difference_y**2
                distance_counts[distance] += 1

            for count in distance_counts.values():
                result += count * (count - 1)

        return result
