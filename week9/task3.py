"""
https://leetcode.com/problems/add-one-row-to-tree/
"""

class Solution(object):
    def addOneRow(self, root, val, depth):
        if depth < 2:
            return TreeNode(val, root)

        def dfs(root, current):
            if root == None:
                return
            current -= 1
            if current == 1:
                root.left = TreeNode(val, root.left, None)
                root.right = TreeNode(val, None, root.right)
            else:
                dfs(root.left, current)
                dfs(root.right, current)

        dfs(root, depth)
        return root
