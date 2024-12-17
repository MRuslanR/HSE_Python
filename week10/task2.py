"""
https://leetcode.com/problems/binary-tree-coloring-game/
"""


class Solution:
    def btreeGameWinningMove(self, root, n, x):
        def dfs(node):
            if node.left:
                left = dfs(node.left)
            else:
                left = 0
            if node.right:
                right = dfs(node.right)
            else:
                right = 0

            cur = left + right + 1
            if node.val == x:
                counts[0], counts[1], counts[2] = cur, left, right
            return cur

        counts = [0, 0, 0]
        dfs(root)

        if (
            n - counts[0] > counts[0]
            or counts[1] > n - counts[1]
            or counts[2] > n - counts[2]
        ):
            return True
        return False
