# 374. Guess Number Higher or Lower

## 思路

答案在 `1` 到 `n` 之间，`guess(mid)` 会告诉我们目标比 `mid` 大还是小。

根据返回值做二分查找，直到找到返回 `0` 的数字。

## 复杂度

- 时间复杂度：`O(log n)`
- 空间复杂度：`O(1)`
