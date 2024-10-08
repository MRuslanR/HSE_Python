"""
https://leetcode.com/problems/maximum-subarray/
"""


class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        s = 0
        mx = 0
        ans = nums[0]
        for i in range(n):
            s += nums[i]
            ans = max(ans, s - mx)
            mx = min(mx, s)
        return ans
