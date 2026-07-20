from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def required_subarrays(maximum_sum: int) -> int:
            subarray_count = 1
            current_sum = 0

            for number in nums:
                if current_sum + number > maximum_sum:
                    subarray_count += 1
                    current_sum = number
                else:
                    current_sum += number

            return subarray_count

        # 第一步：答案一定在最大单个元素与数组总和之间。
        lower_bound = max(nums)
        upper_bound = sum(nums)

        # 第二步：二分能够让分组数量不超过 k 的最小上限。
        while lower_bound < upper_bound:
            middle = (lower_bound + upper_bound) // 2

            if required_subarrays(middle) <= k:
                upper_bound = middle
            else:
                lower_bound = middle + 1

        return lower_bound
