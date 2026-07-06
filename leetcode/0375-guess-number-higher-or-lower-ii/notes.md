# 375. Guess Number Higher or Lower II

## 思路

`dp[left][right]` 表示保证猜中 `[left, right]` 这个区间至少需要多少钱。

如果第一次猜 `guess`，最坏情况会进入左右两边成本更大的那边，所以代价是 `guess + max(left_side, right_side)`。枚举第一次猜的数字取最小。

## 复杂度

- 时间复杂度：`O(n^3)`
- 空间复杂度：`O(n^2)`
