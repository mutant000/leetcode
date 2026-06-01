from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        arrows = 0
        arrow_position = None

        for start, end in points:
            if arrow_position is None or start > arrow_position:
                arrows += 1
                arrow_position = end

        return arrows
