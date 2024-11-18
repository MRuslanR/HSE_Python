"""
https://leetcode.com/problems/new-21-game/
"""


class Solution:
    def new21Game(self, totalPoints, pointsNeeded, maxPoints):
        if pointsNeeded == 0 or totalPoints >= pointsNeeded + maxPoints:
            return 1.0

        dp = [0.0] * (totalPoints + 1)
        cur = 1.0
        result = 0.0

        dp[0] = 1.0

        for i in range(1, totalPoints + 1):
            dp[i] = cur / maxPoints

            if i < pointsNeeded:
                cur += dp[i]
            else:
                result += dp[i]

            if i - maxPoints >= 0:
                cur -= dp[i - maxPoints]

        return result
