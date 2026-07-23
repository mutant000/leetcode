"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        stack = [head]
        previous = None

        while stack:
            current = stack.pop()

            # 第一步：把当前节点接到已经展开好的链表尾部。
            if previous:
                previous.next = current
                current.prev = previous

            # 第二步：先压入 next，再压入 child，让 child 优先被弹出。
            if current.next:
                stack.append(current.next)

            if current.child:
                stack.append(current.child)

            current.child = None
            previous = current

        head.prev = None
        previous.next = None
        return head
