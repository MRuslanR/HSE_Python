"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
"""


class Solution:
    def minOperations(self, nums):
        nums.sort()
        n = len(nums)

        i = 0
        j = 0
        ans = 10**10
        cnt = 0
        while i < n:
            while j + 1 < n and nums[j + 1] - nums[i] <= n - 1:
                j += 1
                if nums[j] == nums[j - 1]:
                    cnt += 1
            ans = min(ans, n - (j - i + 1 - cnt))
            i += 1
            if i < n and nums[i] == nums[i - 1]:
                cnt -= 1

        return ans
