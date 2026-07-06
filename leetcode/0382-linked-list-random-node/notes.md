# 382. Linked List Random Node

## 思路

初始化时把链表值保存到数组里。

每次 `getRandom` 直接从数组中随机选择一个值，所有下标被选中的概率相同。

## 复杂度

- 初始化时间复杂度：`O(n)`
- `getRandom` 时间复杂度：`O(1)`
- 空间复杂度：`O(n)`
