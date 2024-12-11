"""
https://leetcode.com/problems/unique-binary-search-trees/
"""


class Solution:
    def numTrees(self, n):
        T = [0] * (n + 1)
        T[0] = T[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                T[i] += T[j - 1] * T[i - j]

        return T[n]
