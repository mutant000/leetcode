from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        minimum = min(nums)
        maximum = max(nums)

        if minimum == maximum:
            return 0

        bucket_size = max(1, (maximum - minimum) // (len(nums) - 1))
        bucket_count = (maximum - minimum) // bucket_size + 1
        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            index = (num - minimum) // bucket_size

            if buckets[index][0] is None:
                buckets[index] = [num, num]
            else:
                buckets[index][0] = min(buckets[index][0], num)
                buckets[index][1] = max(buckets[index][1], num)

        best = 0
        previous_max = minimum

        for bucket_min, bucket_max in buckets:
            if bucket_min is None:
                continue

            best = max(best, bucket_min - previous_max)
            previous_max = bucket_max

        return best
