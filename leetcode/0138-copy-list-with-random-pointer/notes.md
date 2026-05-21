# 138. Copy List with Random Pointer

## 思路

用原地穿插节点避免额外哈希表：
- 在每个原节点后插入它的复制节点。
- 复制节点的 `random` 可以通过 `original.random.next` 找到。
- 最后把穿插链表拆回原链表和复制链表。

## 复杂度

- Time: `O(n)`
- Space: `O(1)`

## 边界

- 空链表。
- `random` 指向自己。
- 多个节点的 `random` 指向同一个节点。
