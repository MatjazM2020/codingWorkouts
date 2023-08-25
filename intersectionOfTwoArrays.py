from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set(nums1) 
        x = set(nums1).intersection(set(nums2))
        u = []
        for a in x: 
            u.append(a)
        return u

    
        
        
#https://leetcode.com/problems/intersection-of-two-arrays/
#Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

       