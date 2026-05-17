from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        previous = None

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal previous

            if not node:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = previous
            node.left = None
            previous = node

        dfs(root)
