'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        n = len(s)
        j = 0
        st = 0
        for i in range(n):
            while j < i:
                if (s[i]==s[j]):
                    ans = max(ans, j - st)
                    st = j + 1
                    break
                j+=1
            j = st
            ans = max(ans , i-st+1)
        return ans
