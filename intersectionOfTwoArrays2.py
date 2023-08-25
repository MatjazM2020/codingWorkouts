from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        for x in nums1: 
            try: 
                dict1[x] += 1
            except: 
                dict1[x] = 1
        dict2 = {}
        for x in nums2:
            try:  
                dict2[x] += 1
            except: 
                dict2[x] = 1
        res = []
        for x in set(nums1).intersection(set(nums2)): 
            c=  (min(dict1[x], dict2[x]))
            for i in range(c): 
                res.append(x)
        return res
                
        
        
#https://leetcode.com/problems/intersection-of-two-arrays-ii/
#Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.