"""
https://leetcode.com/problems/longest-nice-subarray/
"""


class Solution:
    def longestNiceSubarray(self, nums):
        bits = 0
        left = 0
        ans = 0
        for r in range(len(nums)):
            while bits & nums[r]:
                bits ^= nums[left]
                left += 1
            bits |= nums[r]
            ans = max(ans, r - left + 1)
        return ans
