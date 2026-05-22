# 155. Min Stack

## 思路

用两个栈。`stack` 存真实元素，`minimums` 在每一层存当前栈内最小值。

每次 `push` 时同步压入“加入当前值后的最小值”；`pop` 时两个栈一起弹出。这样 `getMin` 直接返回 `minimums[-1]`。

## 复杂度

- Time: `O(1)` per operation
- Space: `O(n)`

## 边界

- 重复最小值。
- 弹出当前最小值后恢复到前一个最小值。
