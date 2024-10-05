"""

https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        merged = []
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < n:
            merged.append(nums1[i])
            i += 1
        while j < m:
            merged.append(nums2[j])
            j += 1
        return (
            merged[(n + m) // 2]
            if (n + m) % 2 == 1
            else (merged[(n + m) // 2 - 1] + merged[(n + m) // 2] + 0.0) / 2
        )
