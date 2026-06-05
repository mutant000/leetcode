from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        previous = None
        best = float("inf")

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal previous, best

            if not node:
                return

            inorder(node.left)

            if previous is not None:
                best = min(best, node.val - previous)
            previous = node.val

            inorder(node.right)

        inorder(root)
        return best
