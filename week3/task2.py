"""
https://leetcode.com/problems/trapping-rain-water/
"""


class Solution(object):
    def trap(self, height):
        n = len(height)
        left, right = 0, n - 1
        ans = 0
        left_max, right_max = height[0], height[n - 1]
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
        return ans
