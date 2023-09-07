from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dict = {}
        ls = []
        for x in nums:
            max = 0
            for a in str(x): 
                if int(a) > max: 
                    max = int(a)
            ls.append(max)
        max = -1
        for i in range(len(nums)): 
            for j in range(i+1,len(nums)):
                if ls[i] == ls[j] and nums[i]+nums[j]>max:
                    max = nums[i]+nums[j]
        return max 
                    

#https://leetcode.com/problems/max-pair-sum-in-an-array/description/
#You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from 
# nums such that the maximum digit in both numbers are equal. Return the maximum sum or -1 if no such pair exists.