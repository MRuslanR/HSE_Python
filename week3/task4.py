"""
https://leetcode.com/problems/jump-game/
"""


class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        jump = 0
        for i in range(n):
            if jump < 0:
                return 0
            jump = max(jump, nums[i])
            jump -= 1
        return 1
