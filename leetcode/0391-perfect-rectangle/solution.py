from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x, min_y, max_x, max_y = rectangles[0]
        total_area = 0
        odd_corners = set()

        # 第一步：累计小矩形面积，同时更新最外层边界。
        for left, bottom, right, top in rectangles:
            min_x = min(min_x, left)
            min_y = min(min_y, bottom)
            max_x = max(max_x, right)
            max_y = max(max_y, top)
            total_area += (right - left) * (top - bottom)

            # 第二步：内部角会成对出现，使用集合保留出现奇数次的角。
            for corner in (
                (left, bottom),
                (left, top),
                (right, bottom),
                (right, top),
            ):
                if corner in odd_corners:
                    odd_corners.remove(corner)
                else:
                    odd_corners.add(corner)

        outer_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y),
        }
        outer_area = (max_x - min_x) * (max_y - min_y)

        return total_area == outer_area and odd_corners == outer_corners
