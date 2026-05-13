# 35. Search Insert Position

## 思路

题目要找 `target` 应该插入的位置，也就是第一个大于等于 `target` 的下标。

用二分查找维护区间 `[left, right)`：

- 如果 `nums[mid] < target`，说明答案一定在 `mid` 右边。
- 否则 `mid` 可能就是答案，所以保留 `mid`，移动右边界。

## 复杂度

- Time: `O(log n)`
- Space: `O(1)`
