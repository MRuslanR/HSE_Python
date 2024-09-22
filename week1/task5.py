'''
https://leetcode.com/problems/sort-characters-by-frequency/description/
'''


class Solution(object):
    def frequencySort(self, s):
        d = dict()
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sorted_chars = sorted(d.keys(),key=lambda x: d[x])
        sorted_chars = reversed(sorted_chars)
        ans=""
        for i in sorted_chars:
            ans+=i*d[i]
        return ans