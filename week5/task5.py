"""
https://leetcode.com/problems/brick-wall/
"""


class Solution:
    def leastBricks(self, wall):
        d = dict()
        n = len(wall)
        d[0] = 0
        for line in wall:
            cur = 0
            for brick in line[:-1]:
                cur += brick
                if cur not in d:
                    d[cur] = 0
                d[cur] += 1

        return min([n - d[key] for key in d])
