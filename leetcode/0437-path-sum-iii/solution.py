from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_count = {0: 1}

        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0

            current_sum += node.val
            paths = prefix_count.get(current_sum - targetSum, 0)
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

            paths += dfs(node.left, current_sum)
            paths += dfs(node.right, current_sum)

            prefix_count[current_sum] -= 1
            if prefix_count[current_sum] == 0:
                del prefix_count[current_sum]
            return paths

        return dfs(root, 0)
