from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bucket_size = valueDiff + 1
        buckets = {}

        for index, num in enumerate(nums):
            bucket_id = num // bucket_size

            if bucket_id in buckets:
                return True
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True

            buckets[bucket_id] = num

            if index >= indexDiff:
                old_bucket_id = nums[index - indexDiff] // bucket_size
                del buckets[old_bucket_id]

        return False
