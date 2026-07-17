from heapq import heappop, heappush
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        row_count = len(heightMap)
        column_count = len(heightMap[0])
        if row_count < 3 or column_count < 3:
            return 0

        visited = [
            [False] * column_count
            for _ in range(row_count)
        ]
        boundary_heap = []

        def add_boundary_cell(row: int, column: int) -> None:
            if visited[row][column]:
                return

            visited[row][column] = True
            heappush(
                boundary_heap,
                (heightMap[row][column], row, column),
            )

        # 第一步：把四周边界作为不能存水的初始围墙。
        for row in range(row_count):
            add_boundary_cell(row, 0)
            add_boundary_cell(row, column_count - 1)
        for column in range(1, column_count - 1):
            add_boundary_cell(0, column)
            add_boundary_cell(row_count - 1, column)

        trapped_water = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # 第二步：始终从当前最低边界向内部扩展。
        while boundary_heap:
            boundary_height, row, column = heappop(boundary_heap)

            for row_change, column_change in directions:
                next_row = row + row_change
                next_column = column + column_change

                if not (
                    0 <= next_row < row_count
                    and 0 <= next_column < column_count
                ):
                    continue
                if visited[next_row][next_column]:
                    continue

                visited[next_row][next_column] = True
                neighbor_height = heightMap[next_row][next_column]

                # 第三步：低洼处存水，并以较高者作为新的有效边界。
                trapped_water += max(0, boundary_height - neighbor_height)
                heappush(
                    boundary_heap,
                    (
                        max(boundary_height, neighbor_height),
                        next_row,
                        next_column,
                    ),
                )

        return trapped_water
