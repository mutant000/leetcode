# 153. Find Minimum in Rotated Sorted Array

## 思路

最小值一定在旋转断点处。

用二分比较 `nums[mid]` 和 `nums[right]`：
- 如果 `nums[mid] > nums[right]`，说明最小值在 `mid` 右边。
- 否则，`mid` 可能就是最小值，或者最小值在 `mid` 左边。

不断缩小范围，最后 `left == right` 的位置就是最小值。

## 复杂度

- Time: `O(log n)`
- Space: `O(1)`

## 边界

- 数组没有旋转。
- 数组长度为 1。
- 最小值在最后一个位置。
