from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = len(nums)
        res = 0
        if l%2 == 0: 
            for i in range((l//2)): 
                res += int(str(nums[i])+str(nums[l-i-1]))
        else:
            res += nums[l//2]
            for i in range((l//2)): 
                res += int(str(nums[i])+str(nums[l-i-1]))
        return res
    
    
    
    
#https://leetcode.com/problems/find-the-array-concatenation-value/description/
#You are given a 0-indexed integer array nums.
#The concatenation of two numbers is the number formed by concatenating their numerals.
#For example, the concatenation of 15, 49 is 1549.
#The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:
#If there exists more than one number in nums, pick the first element and last element in nums respectively and
# add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.
#If one element exists, add its value to the concatenation value of nums, then delete it.
#Return the concatenation value of the nums.

