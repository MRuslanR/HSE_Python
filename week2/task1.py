"""
https://leetcode.com/problems/group-anagrams/description/

"""


class Solution(object):
    def groupAnagrams(self, strs):

        d = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in d:
                d[sorted_word] = []
            d[sorted_word].append(word)

        ans = []
        for i in d:
            ans.append(list(d[i]))
        return ans
