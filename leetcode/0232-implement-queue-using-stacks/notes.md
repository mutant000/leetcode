# Implement Queue using Stacks

## 思路

用两个栈模拟队列。

`in_stack` 负责接收新元素，`out_stack` 负责弹出队首元素。需要 `pop` 或 `peek` 时，如果 `out_stack` 为空，就把 `in_stack` 中的元素倒过去，这样顺序就从后进先出变成先进先出。

## 复杂度

- 时间复杂度：均摊 `O(1)`
- 空间复杂度：`O(n)`
