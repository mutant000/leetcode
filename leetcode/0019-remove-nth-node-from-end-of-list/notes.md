# 19. Remove Nth Node From End of List

## 思路

使用快慢指针，保持 `right` 比 `left` 先走 `n + 1` 步（带 `dummy` 节点）。

这样 `right` 到尾部时，`left.next` 就是倒数第 `n` 个节点，需要被删除。

1. `dummy.next = head`，`left = right = dummy`。
2. `right` 先走 `n+1` 步。
3. 两指针一起移动，直到 `right` 为 `None`。
4. 删除 `left.next`：`left.next = left.next.next`。

## 复杂度

- Time: `O(L)`，`L` 为链表长度
- Space: `O(1)`

## 边界

- `n` 等于链表长度时，删除头结点（`dummy` 可安全处理）。
- 链表仅一节点、或删除尾节点都正常。
