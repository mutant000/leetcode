from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        heights = [0] * len(matrix[0])
        best = 0

        def largest_rectangle_area(values: List[int]) -> int:
            stack = []
            max_area = 0

            for index in range(len(values) + 1):
                current = values[index] if index < len(values) else 0

                while stack and values[stack[-1]] > current:
                    height = values[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = index - left - 1
                    max_area = max(max_area, height * width)

                stack.append(index)

            return max_area

        for row in matrix:
            for col, value in enumerate(row):
                if value == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            best = max(best, largest_rectangle_area(heights))

        return best
