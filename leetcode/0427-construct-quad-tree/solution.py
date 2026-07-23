from typing import List


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        size = len(grid)
        prefix_sum = [[0] * (size + 1) for _ in range(size + 1)]

        # 第一步：建立二维前缀和，之后可以 O(1) 判断一个区域是否全相同。
        for row in range(1, size + 1):
            row_sum = 0
            for column in range(1, size + 1):
                row_sum += grid[row - 1][column - 1]
                prefix_sum[row][column] = (
                    prefix_sum[row - 1][column] + row_sum
                )

        def region_sum(row: int, column: int, length: int) -> int:
            bottom = row + length
            right = column + length
            return (
                prefix_sum[bottom][right]
                - prefix_sum[row][right]
                - prefix_sum[bottom][column]
                + prefix_sum[row][column]
            )

        # 第二步：区域全为 0 或全为 1 时创建叶子，否则递归分成四块。
        def build(row: int, column: int, length: int) -> "Node":
            total = region_sum(row, column, length)

            if total == 0:
                return Node(False, True, None, None, None, None)

            if total == length * length:
                return Node(True, True, None, None, None, None)

            half = length // 2
            return Node(
                True,
                False,
                build(row, column, half),
                build(row, column + half, half),
                build(row + half, column, half),
                build(row + half, column + half, half),
            )

        return build(0, 0, size)
