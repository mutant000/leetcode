from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_by_value = {value: index for index, value in enumerate(inorder)}
        preorder_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)
            inorder_index = index_by_value[root_value]
            root.left = build(left, inorder_index - 1)
            root.right = build(inorder_index + 1, right)
            return root

        return build(0, len(inorder) - 1)
