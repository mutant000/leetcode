# 334. Increasing Triplet Subsequence

## 思路

维护当前见过的最小值 `first`，以及能作为第二个数的最小值 `second`。

如果遇到一个数比 `second` 还大，就找到了递增三元组。

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`
