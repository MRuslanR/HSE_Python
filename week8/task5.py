"""
https://leetcode.com/problems/count-number-of-nice-subarrays/
"""


class Solution:
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        d = dict()
        d[0] = 1
        current = 0
        result = 0

        for i in range(n):
            if nums[i] % 2 == 1:
                current += 1
            if (current - k) in d:
                result += d[current - k]
            if current not in d:
                d[current] = 0
            d[current] += 1

        return result
