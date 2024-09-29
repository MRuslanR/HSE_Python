"""
https://leetcode.com/problems/zigzag-conversion/
"""


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        n = len(s)
        ans = [""] * numRows
        row = 0
        lift = 1
        for i in range(n):
            ans[row] += s[i]
            if row == numRows - 1:
                lift = -1
            if row == 0:
                lift = 1
            row += lift
        answer = ""
        for i in range(numRows):
            answer += ans[i]
        return answer
