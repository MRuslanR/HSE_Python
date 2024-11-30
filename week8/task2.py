"""
https://leetcode.com/problems/k-radius-subarray-averages/
"""


class Solution:
    def getAverages(self, nums, k):
        n = len(nums)
        length = 2 * k + 1

        ans = [-1] * n
        s = 0
        j = 0

        for i in range(n):
            s += nums[i]
            if i - j + 1 > length:
                s -= nums[j]
                j += 1
            if i - j + 1 == length:
                ans[k + j] = s // length
        return ans
