# 315. Count of Smaller Numbers After Self

## 思路

从右往左扫描。右边已经出现过的数放进树状数组里。

当前数的排名是 `rank`，查询 `rank - 1` 的前缀和，就能知道右边有多少数比它小。

## 复杂度

- 时间复杂度：`O(n log n)`
- 空间复杂度：`O(n)`
