"""
https://leetcode.com/problems/minimum-window-substring/
"""


class Solution:
    def minWindow(self, s, t):
        arr = [0] * 128
        if len(s) < len(t):
            return ""
        for char in t:
            arr[ord(char)] += 1

        cnt = 0
        start = 0
        minLen = 10**10
        minStart = 0
        for i in range(len(s)):
            if arr[ord(s[i])] > 0:
                cnt += 1
            arr[ord(s[i])] -= 1
            while cnt == len(t):
                if minLen > i - start + 1:
                    minLen = i - start + 1
                    minStart = start
                if arr[ord(s[start])] == 0:
                    cnt -= 1
                arr[ord(s[start])] += 1
                start += 1

        return s[minStart : minStart + minLen] if minLen != 10**10 else ""
