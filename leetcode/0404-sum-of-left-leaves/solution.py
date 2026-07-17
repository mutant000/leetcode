from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_leaf_sum = 0
        stack = [(root, False)]

        while stack:
            node, is_left_child = stack.pop()

            if not node.left and not node.right:
                if is_left_child:
                    left_leaf_sum += node.val
                continue

            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, True))

        return left_leaf_sum
