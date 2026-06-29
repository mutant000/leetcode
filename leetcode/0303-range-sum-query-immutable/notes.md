# 303. Range Sum Query - Immutable

## 思路

预处理前缀和。`prefix[i]` 表示前 `i` 个数的和。

区间 `[left, right]` 的和就是 `prefix[right + 1] - prefix[left]`。

## 复杂度

- 初始化时间复杂度：`O(n)`
- 查询时间复杂度：`O(1)`
- 空间复杂度：`O(n)`
