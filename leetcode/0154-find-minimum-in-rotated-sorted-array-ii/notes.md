# Find Minimum in Rotated Sorted Array II

## 思路

二分查找旋转数组中的最小值。

比较 `nums[mid]` 和 `nums[right]`：

- 如果 `nums[mid] > nums[right]`，最小值在右半边。
- 如果 `nums[mid] < nums[right]`，最小值在左半边或就是 `mid`。
- 如果相等，无法判断哪边有序，但可以安全丢掉 `right`。

## 复杂度

- 平均时间复杂度：`O(log n)`
- 最坏时间复杂度：`O(n)`，大量重复元素时退化
- 空间复杂度：`O(1)`
