from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy = ListNode()
        large_dummy = ListNode()
        small = small_dummy
        large = large_dummy

        current = head
        while current:
            next_node = current.next
            current.next = None

            if current.val < x:
                small.next = current
                small = small.next
            else:
                large.next = current
                large = large.next

            current = next_node

        small.next = large_dummy.next
        return small_dummy.next
