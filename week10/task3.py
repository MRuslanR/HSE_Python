"""
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
"""


class Solution(object):
    def countPairs(self, root, distance):
        ans = [0]

        def dfs(node):
            if not node:
                return []
            if not (node.left or node.right):
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for i in left:
                for j in right:
                    if i + j <= distance:
                        ans[0] += 1
            return [i + 1 for i in left + right]

        dfs(root)
        return ans[0]
