from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []

        for value in range(1 << n):
            result.append(value ^ (value >> 1))

        return result
