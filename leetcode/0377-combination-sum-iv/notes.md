# 377. Combination Sum IV

## 思路

题目把不同顺序算作不同组合，所以外层枚举目标和，内层枚举最后一个选择的数字。

`dp[total]` 表示凑出 `total` 的排列数量。

## 复杂度

- 时间复杂度：`O(target * n)`
- 空间复杂度：`O(target)`
