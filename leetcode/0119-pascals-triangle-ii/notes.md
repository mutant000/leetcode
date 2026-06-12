# Pascal's Triangle II

## 思路

用一维数组滚动生成杨辉三角的指定行。

每生成下一行，先在末尾补 `1`，再从右往左更新中间位置：

```text
row[index] = row[index] + row[index - 1]
```

必须倒序更新，避免当前行的新值影响后面的计算。

## 复杂度

- 时间复杂度：`O(rowIndex^2)`
- 空间复杂度：`O(rowIndex)`
