from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        index_by_value = {value: index for index, value in enumerate(inorder)}
        postorder_index = len(postorder) - 1

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal postorder_index

            if left > right:
                return None

            root_value = postorder[postorder_index]
            postorder_index -= 1
            root = TreeNode(root_value)
            inorder_index = index_by_value[root_value]

            root.right = build(inorder_index + 1, right)
            root.left = build(left, inorder_index - 1)
            return root

        return build(0, len(inorder) - 1)
