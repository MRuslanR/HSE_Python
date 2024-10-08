"""
https://leetcode.com/problems/jump-game-ii/description/
"""


class Solution:
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        jumps = 0
        gas = nums[0]

        profit = -1
        profit_ind = -1
        profit_gas = -1

        i = 0
        while i < n:
            for j in range(i, i + gas + 1):
                if j == n - 1:
                    return jumps + 1
                if profit <= nums[j] + j:
                    profit = j + nums[j]
                    profit_ind = j
                    profit_gas = nums[j]

            gas = profit_gas
            i = profit_ind
            jumps += 1
        return jumps
