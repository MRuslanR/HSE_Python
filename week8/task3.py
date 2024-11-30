"""
https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
"""


class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        ans = 0
        cur = 0
        start, end = 0, 0
        s = 0

        while end < n:
            s += nums[end]
            end += 1
            cur += 1

            while s * cur >= k:
                s -= nums[start]
                start += 1
                cur -= 1
                ans += cur

        ans += (cur * (cur + 1)) // 2
        return ans
