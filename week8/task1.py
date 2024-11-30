"""
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays
"""


class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        n = len(nums)
        pr = [0] * (n + 1)

        for i in range(n):
            pr[i + 1] = pr[i] + nums[i]

        maxFirst, maxSecond = 0, 0
        ans = 0

        for i in range(firstLen + secondLen, n + 1):
            maxFirst = max(maxFirst, pr[i - secondLen] - pr[i - secondLen - firstLen])
            maxSecond = max(maxSecond, pr[i - firstLen] - pr[i - firstLen - secondLen])
            ans = max(
                ans,
                max(
                    maxFirst + pr[i] - pr[i - secondLen],
                    maxSecond + pr[i] - pr[i - firstLen],
                ),
            )

        return ans
