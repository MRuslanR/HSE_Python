"""
https://leetcode.com/problems/subarray-product-less-than-k/
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0 or k == 1:
            return 0
        n = len(nums)
        i, j = 0, 0
        cur = 1
        count = 0
        while j < n:
            cur *= nums[j]
            while cur >= k:
                cur /= nums[i]
                i += 1
            count += j - i + 1
            j += 1
        return count
