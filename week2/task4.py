"""
https://leetcode.com/problems/decoded-string-at-index/description/

"""


class Solution(object):
    def decodeAtIndex(self, s, k):
        ind = 0
        n = len(s)
        for i in s:
            if ord(i) <= 57:
                ind *= int(i)
            else:
                ind += 1
        for i in range(n - 1, -1, -1):
            if ord(s[i]) <= 57:
                ind /= int(s[i])
                k = k % ind
            else:
                if k == ind or k == 0:
                    return s[i]
                ind -= 1
