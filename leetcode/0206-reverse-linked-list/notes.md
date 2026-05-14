# 206. Reverse Linked List

## 思路

用三个指针原地反转链表。

1. `prev` 表示已经反转好的前半段头节点，初始为 `None`。
2. `current` 扫描原链表。
3. 每次先保存 `current.next`，再把 `current.next` 指向 `prev`。
4. 向前移动 `prev` 和 `current`，直到原链表遍历完成。

最后 `prev` 就是反转后的新头节点。

## 复杂度

- Time: `O(n)`
- Space: `O(1)`

## 边界

- 空链表返回 `None`。
- 只有一个节点时，反转后仍然是自己。
- 反转前必须先保存下一个节点，否则会丢失剩余链表。
