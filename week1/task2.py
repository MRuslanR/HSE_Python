"""
https://leetcode.com/problems/minimum-window-substring/description/

"""


class Solution(object):
    def minWindow(self, s, t):
        arr = [0] * 128
        if len(s) < len(t):
            return ""
        for i in range(len(t)):
            arr[ord(t[i])] += 1

        cnt = 0
        start = 0
        minLen = 0
        minStart = 0
        for i in range(len(s)):
            if arr[ord(s[i])] > 0:
                cnt += 1
            arr[ord(s[i])] -= 1
            while cnt == len(t):
                if minLen > i - start + 1 or minLen == 0:
                    minLen = i - start + 1
                    minStart = start
                if arr[ord(s[start])] == 0:
                    cnt -= 1
                arr[ord(s[start])] += 1
                start += 1

        print(minStart, minLen)
        return s[minStart : minStart + minLen]
