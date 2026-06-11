# N-Queens II

## 思路

用位运算回溯统计方案数。

每一行只放一个皇后，`columns` 记录已经被占用的列，`diagonals` 和 `anti_diagonals` 记录两类对角线攻击范围。

当前行可放的位置是：

```text
full_mask & ~(columns | diagonals | anti_diagonals)
```

每次取最低位的一个可用位置继续递归。

## 复杂度

- 时间复杂度：约 `O(n!)`
- 空间复杂度：`O(n)`
