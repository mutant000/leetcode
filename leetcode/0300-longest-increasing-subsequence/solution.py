from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for number in nums:
            index = bisect_left(tails, number)
            if index == len(tails):
                tails.append(number)
            else:
                tails[index] = number

        return len(tails)
