"""
https://leetcode.com/problems/constrained-subsequence-sum/
"""

from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums, k):
        dq = deque()
        n = len(nums)
        for i in range(n):
            if dq:
                nums[i] += nums[dq[0]]

            while dq and (i - dq[0] >= k or nums[i] >= nums[dq[-1]]):
                if nums[i] >= nums[dq[-1]]:
                    dq.pop()
                else:
                    dq.popleft()

            if nums[i] > 0:
                dq.append(i)

        return max(nums)
