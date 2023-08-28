from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = set(nums)
        srtd = sorted(x,reverse = True)
        if len(srtd) > 2: 
         return srtd[2]
        elif len(srtd) == 2 or len(srtd) == 1:
         return srtd[0]
        else:
         return 0
        
        
#https://leetcode.com/problems/third-maximum-number/
#Given an integer array nums, return the third distinct maximum number 
# in this array. If the third maximum does not exist, return the maximum number.