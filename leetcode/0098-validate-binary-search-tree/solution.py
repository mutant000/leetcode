from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        current = root
        previous = None

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if previous is not None and current.val <= previous:
                return False

            previous = current.val
            current = current.right

        return True
