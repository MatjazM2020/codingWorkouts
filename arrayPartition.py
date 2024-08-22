from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return sum(nums[i] for i in range(0, n, 2))
    
    
    
'''
https://leetcode.com/problems/array-partition/description/

Given an integer array nums of 2n integers, group these integers into n pairs 
(a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
'''