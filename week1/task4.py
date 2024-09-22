'''

https://leetcode.com/problems/largest-number/description/
'''

from functools import cmp_to_key
def comparator(a, b):
    if str(a) + str(b) > str(b) + str(a):
        return -1
    return 1
class Solution(object):
    def largestNumber(self, nums):
        nums = sorted(nums,key=cmp_to_key(comparator))
        ans = ""
        for i in range(len(nums)):
            ans+=str(nums[i])
        if ans[0]=="0": return "0"
        return ans
