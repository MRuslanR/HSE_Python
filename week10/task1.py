"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""


class Solution:
    def flatten(self, root):
        if not root:
            return None

        stack = [root]
        while len(stack):
            root = stack.pop()

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

            root.left = None
            if len(stack):
                root.right = stack[-1]
            else:
                root.right = None
