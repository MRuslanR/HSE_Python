"""
https://leetcode.com/problems/merge-intervals/
"""


class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        ans = []
        start = intervals[0][0]
        finish = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > finish:
                ans.append([start, finish])
                start = intervals[i][0]
            if intervals[i][1] > finish:
                finish = intervals[i][1]
        ans.append([start, finish])
        return ans
