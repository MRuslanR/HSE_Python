"""
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
"""


class Solution:
    def minSwaps(self, nums):
        total = 0
        cur = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                total += 1

        for i in range(total):
            if nums[i] == 1:
                cur += 1

        mx = cur
        for i in range(total, total + n):
            cur = cur + nums[i % n] - nums[(i - total) % n]
            mx = max(mx, cur)

        return total - mx
