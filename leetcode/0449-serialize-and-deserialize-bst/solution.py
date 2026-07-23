from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""

        values = []
        stack = [root]

        while stack:
            node = stack.pop()
            values.append(str(node.val))

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return " ".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        values = [int(value) for value in data.split()]
        root = TreeNode(values[0])
        stack = [root]

        for value in values[1:]:
            node = TreeNode(value)

            if value < stack[-1].val:
                stack[-1].left = node
            else:
                parent = None

                while stack and value > stack[-1].val:
                    parent = stack.pop()

                parent.right = node

            stack.append(node)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
