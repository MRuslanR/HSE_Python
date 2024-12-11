"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""


class Solution:
    def maxAncestorDiff(self, root):
        max_val = root.val
        min_val = root.val
        return self.findMax(root, min_val, max_val)

    def findMax(self, root, min_val, max_val):
        if not root:
            return abs(max_val - min_val)

        left = self.findMax(
            root.left, min(min_val, root.val), max_val=max(max_val, root.val)
        )
        right = self.findMax(
            root.right, min(min_val, root.val), max_val=max(max_val, root.val)
        )

        return max(left, right)
