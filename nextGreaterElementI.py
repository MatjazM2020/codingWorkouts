from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        x = []
        for i in range(m):
            for j in range(n): 
                if nums1[i] == nums2[j]: 
                    for k in range(j,n):
                        if nums2[k] > nums1[i]: 
                            x.append(nums2[k])
                            break
                        elif k == n-1: 
                            x.append(-1)
                            break
        return x
    

#https://leetcode.com/problems/next-greater-element-i/
#The next greater element of some element x in an array is the first greater element that 
# is to the right of x in the same array.
#You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a
# subset of nums2. For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
# and determine the next greater element of nums2[j] in nums2. If there is no next greater element, 
# then the answer for this query is -1. Return an array ans of length nums1.length such that ans[i]
# is the next greater element as described above.

