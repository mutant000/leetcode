from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        row_count = len(heights)
        column_count = len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def reachable_from_ocean(starting_cells):
            reachable = set(starting_cells)
            stack = list(reachable)

            while stack:
                row, column = stack.pop()

                for row_change, column_change in directions:
                    next_row = row + row_change
                    next_column = column + column_change

                    if not (
                        0 <= next_row < row_count
                        and 0 <= next_column < column_count
                    ):
                        continue
                    if (next_row, next_column) in reachable:
                        continue
                    if heights[next_row][next_column] < heights[row][column]:
                        continue

                    reachable.add((next_row, next_column))
                    stack.append((next_row, next_column))

            return reachable

        # 第一步：从两片海洋边界反向走向不低于当前高度的格子。
        pacific_starts = (
            [(0, column) for column in range(column_count)]
            + [(row, 0) for row in range(row_count)]
        )
        atlantic_starts = (
            [(row_count - 1, column) for column in range(column_count)]
            + [(row, column_count - 1) for row in range(row_count)]
        )

        pacific_reachable = reachable_from_ocean(pacific_starts)
        atlantic_reachable = reachable_from_ocean(atlantic_starts)

        # 第二步：同时能被两次反向搜索到的格子就是答案。
        return [
            [row, column]
            for row in range(row_count)
            for column in range(column_count)
            if (
                (row, column) in pacific_reachable
                and (row, column) in atlantic_reachable
            )
        ]
