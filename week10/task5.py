"""
https://leetcode.com/problems/binary-tree-pruning/
"""


class Solution:
    def pruneTree(self, root):
        stack = [(root, False)]
        d = set()
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if node.left in d:
                        node.left = None
                    if node.right in d:
                        node.right = None
                    if node.val == 0 and node.left is None and node.right is None:
                        d.add(node)
                else:
                    stack.extend(
                        [(node, True), (node.left, False), (node.right, False)]
                    )

        if root not in d:
            return root
        return None
