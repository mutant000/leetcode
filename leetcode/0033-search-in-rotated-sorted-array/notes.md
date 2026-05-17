# 33. Search in Rotated Sorted Array

## 思路

旋转后的数组仍然可以二分，因为每次取中点时，左右两半至少有一半是有序的。

比较 `nums[left]` 和 `nums[mid]`：
- 如果左半段有序，就判断 `target` 是否落在 `nums[left]` 到 `nums[mid]` 之间。
- 如果右半段有序，就判断 `target` 是否落在 `nums[mid]` 到 `nums[right]` 之间。

目标在哪一侧，就保留哪一侧；否则丢掉那一侧。

## 复杂度

- Time: `O(log n)`
- Space: `O(1)`

## 边界

- 数组长度为 1。
- 没有旋转。
- `target` 不存在。
