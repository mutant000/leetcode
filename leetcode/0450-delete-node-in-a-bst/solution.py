from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(
        self,
        root: Optional[TreeNode],
        key: int,
    ) -> Optional[TreeNode]:
        parent = None
        node = root

        while node and node.val != key:
            parent = node

            if key < node.val:
                node = node.left
            else:
                node = node.right

        if not node:
            return root

        if node.left and node.right:
            successor_parent = node
            successor = node.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            node.val = successor.val
            parent = successor_parent
            node = successor

        child = node.left if node.left else node.right

        if not parent:
            return child

        if parent.left is node:
            parent.left = child
        else:
            parent.right = child

        return root
