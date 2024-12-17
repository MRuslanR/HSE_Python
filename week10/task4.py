"""
https://leetcode.com/problems/maximum-binary-tree-ii/
"""


class Solution(object):
    def insertIntoMaxTree(self, root, val):
        def dfs(curr):
            if not curr:
                return []
            return dfs(curr.left) + [curr.val] + dfs(curr.right)

        def build(vals):
            if not vals:
                return None
            num = max(vals)
            idx = vals.index(num)
            node = TreeNode(num, build(vals[:idx]), build(vals[idx + 1 :]))
            return node

        return build(dfs(root) + [val])
