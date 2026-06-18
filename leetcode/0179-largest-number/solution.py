from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(left: str, right: str) -> int:
            if left + right > right + left:
                return -1
            if left + right < right + left:
                return 1
            return 0

        parts = sorted((str(num) for num in nums), key=cmp_to_key(compare))
        answer = "".join(parts)

        return "0" if answer[0] == "0" else answer
