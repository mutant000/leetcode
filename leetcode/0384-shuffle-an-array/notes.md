# 384. Shuffle an Array

## 思路

保存原数组副本，`reset` 返回原始顺序。

`shuffle` 使用 Fisher-Yates 洗牌：从后往前，每个位置随机选择一个还没有固定的位置交换。

## 复杂度

- `reset` 时间复杂度：`O(n)`
- `shuffle` 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`
