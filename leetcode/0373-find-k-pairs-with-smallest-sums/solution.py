import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        result = []

        for index in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[index] + nums2[0], index, 0))

        while heap and len(result) < k:
            _, index1, index2 = heapq.heappop(heap)
            result.append([nums1[index1], nums2[index2]])

            if index2 + 1 < len(nums2):
                heapq.heappush(heap, (nums1[index1] + nums2[index2 + 1], index1, index2 + 1))

        return result
