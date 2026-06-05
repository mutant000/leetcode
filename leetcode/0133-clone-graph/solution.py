from typing import Optional


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if not node:
            return None

        clones = {}

        def clone(current: 'Node') -> 'Node':
            if current in clones:
                return clones[current]

            copied = Node(current.val)
            clones[current] = copied

            for neighbor in current.neighbors:
                copied.neighbors.append(clone(neighbor))

            return copied

        return clone(node)
