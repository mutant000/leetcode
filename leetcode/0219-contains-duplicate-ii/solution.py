from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}

        for index, num in enumerate(nums):
            if num in last_index and index - last_index[num] <= k:
                return True

            last_index[num] = index

        return False
