from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0

        for index, height in enumerate(heights + [0]):
            start = index

            while stack and stack[-1][1] > height:
                previous_index, previous_height = stack.pop()
                best = max(best, previous_height * (index - previous_index))
                start = previous_index

            stack.append((start, height))

        return best
