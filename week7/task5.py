"""
https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
"""


class Solution:
    def maxSubarrayLength(self, nums, k):
        s = {}
        n = len(nums)
        left = 0
        r = 0
        ans = 0
        while r < n:
            if nums[r] not in s:
                s[nums[r]] = 0
            s[nums[r]] += 1

            while s[nums[r]] > k:
                s[nums[left]] -= 1
                if s[nums[left]] == 0:
                    del s[nums[left]]
                left += 1
            ans = max(ans, r - left + 1)
            r += 1
        return ans
