from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self._reverse(slow)
        first_half = head
        current = second_half
        is_palindrome = True

        while current:
            if first_half.val != current.val:
                is_palindrome = False
                break
            first_half = first_half.next
            current = current.next

        self._reverse(second_half)
        return is_palindrome

    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
