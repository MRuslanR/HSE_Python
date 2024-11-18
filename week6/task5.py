"""
https://leetcode.com/problems/permutation-in-string/
"""


class Solution:
    def checkInclusion(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        i, j = 0, 0
        count1, count2 = [0] * 26, [0] * 26

        for char in s1:
            count1[ord(char) - ord("a")] += 1

        while j < len1:
            count2[ord(s2[j]) - ord("a")] += 1
            j += 1

        if count1 == count2:
            return True

        while j < len2:
            count2[ord(s2[j]) - ord("a")] += 1
            count2[ord(s2[i]) - ord("a")] -= 1
            j += 1
            i += 1

            if count1 == count2:
                return True

        return False
