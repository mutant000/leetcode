# 430. Flatten a Multilevel Doubly Linked List

## 思路

展开顺序相当于深度优先遍历：访问当前节点后，先访问 `child` 链表，再回到原来的 `next`。

使用栈模拟 DFS。因为栈后进先出，所以先压入 `next`，再压入 `child`。每次弹出节点时，把它接到已展开链表的末尾，并清空 `child`。

最后保证头节点的 `prev` 和尾节点的 `next` 都是 `None`。

## 复杂度

- 时间复杂度：`O(n)`
- 空间复杂度：`O(n)`，最坏情况下栈中保存多个待处理节点
