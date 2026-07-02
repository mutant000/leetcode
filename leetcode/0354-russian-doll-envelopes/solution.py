from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))
        lis = []

        for _, height in envelopes:
            index = bisect_left(lis, height)
            if index == len(lis):
                lis.append(height)
            else:
                lis[index] = height

        return len(lis)
