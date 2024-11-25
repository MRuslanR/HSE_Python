"""
https://leetcode.com/problems/find-the-longest-equal-subarray/
"""


class Solution:
    def longestEqualSubarray(self, nums, k):
        left = 0
        r = 0
        n = len(nums)
        mx = 0
        d = {}
        while r < n:
            if nums[r] in d:
                d[nums[r]] += 1
            else:
                d[nums[r]] = 1
            mx = max(mx, d[nums[r]])
            del_count = (r - left + 1) - mx
            if del_count > k:
                d[nums[left]] -= 1
                if d[nums[left]] == 0:
                    del d[nums[left]]
                left += 1
            r += 1
        return mx
