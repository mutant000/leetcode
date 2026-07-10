from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        number_count = len(nums)
        total_sum = sum(nums)
        current_value = sum(index * number for index, number in enumerate(nums))
        maximum_value = current_value

        # 每次把末尾元素移到开头，用上一轮结果在 O(1) 时间得到新值。
        for rotation in range(1, number_count):
            moved_number = nums[-rotation]
            current_value += total_sum - number_count * moved_number
            maximum_value = max(maximum_value, current_value)

        return maximum_value
