"""
https://leetcode.com/problems/triangle/
"""


class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        dp = [[0] * (i + 1) for i in range(n)]

        dp[0][0] = triangle[0][0]

        dp[1][0] = dp[0][0] + triangle[1][0]
        dp[1][1] = dp[0][0] + triangle[1][1]

        for i in range(2, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        return min(dp[n - 1])
