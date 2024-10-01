from typing import List



class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        if mx%mn == 0:
            return mn
        for i in range(1,mn):
            if mn%i==0 and mx%i==0:
                res = i
        return res
    
    
    
    
'''
https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/

Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
'''