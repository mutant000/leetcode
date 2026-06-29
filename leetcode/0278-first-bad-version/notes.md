# 278. First Bad Version

## 思路

坏版本之后的版本都会是坏的，所以答案具有单调性。

二分查找第一个 `isBadVersion(mid)` 为 `True` 的位置。

## 复杂度

- 时间复杂度：`O(log n)`
- 空间复杂度：`O(1)`
