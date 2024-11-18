"""
https://leetcode.com/problems/sliding-window-maximum/
"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
        dq = deque()
        n = len(nums)
        for i in range(k):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        if dq:
            ans.append(nums[dq[0]])
        for i in range(k, n):
            element = nums[i]
            if dq and i - k + 1 > dq[0]:
                dq.popleft()
            while dq and element > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if dq:
                ans.append(nums[dq[0]])
        return ans
