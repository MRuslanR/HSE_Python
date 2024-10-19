"""
https://leetcode.com/problems/contiguous-array/
"""


class Solution:
    def findMaxLength(self, nums):
        d = dict()
        sm = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                sm += -1
            else:
                sm += 1

            if sm == 0:
                max_len = max(max_len, i + 1)
            elif sm in d:
                max_len = max(max_len, i - d[sm])
            else:
                d[sm] = i

        return max_len
