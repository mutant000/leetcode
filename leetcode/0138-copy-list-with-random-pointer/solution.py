from typing import Optional


# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        while current:
            copied = Node(current.val, current.next)
            current.next = copied
            current = copied.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        current = head
        copied_head = head.next
        while current:
            copied = current.next
            current.next = copied.next
            copied.next = copied.next.next if copied.next else None
            current = current.next

        return copied_head
