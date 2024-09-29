"""
https://leetcode.com/problems/string-compression/description/

"""


class Solution(object):
    def compress(self, chars):
        cur = 1
        ans = 0

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                cur += 1
            else:
                ans += 1
                if cur != 1:
                    for ind in str(cur):
                        chars[ans] = ind
                        ans += 1
                chars[ans] = chars[i]
                cur = 1

        ans += 1
        if cur != 1:
            for ind in str(cur):
                chars[ans] = ind
                ans += 1

        return ans
