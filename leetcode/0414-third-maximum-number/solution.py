from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = None
        second = None
        third = None

        for number in nums:
            if number == first or number == second or number == third:
                continue

            if first is None or number > first:
                third = second
                second = first
                first = number
            elif second is None or number > second:
                third = second
                second = number
            elif third is None or number > third:
                third = number

        return third if third is not None else first
