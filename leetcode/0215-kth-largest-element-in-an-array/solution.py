from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = k - 1
        left = 0
        right = len(nums) - 1

        while True:
            pivot = nums[(left + right) // 2]
            greater = left
            index = left
            smaller = right

            while index <= smaller:
                if nums[index] > pivot:
                    nums[greater], nums[index] = nums[index], nums[greater]
                    greater += 1
                    index += 1
                elif nums[index] < pivot:
                    nums[index], nums[smaller] = nums[smaller], nums[index]
                    smaller -= 1
                else:
                    index += 1

            if target < greater:
                right = greater - 1
            elif target > smaller:
                left = smaller + 1
            else:
                return pivot
