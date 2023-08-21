from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         if len(nums) == 1: 
            return nums[0]
         max = 0
         maxElt = 0
         dict = {}
         for x in nums: 
            if x in dict:
               dict[x] += 1
               if dict[x] > max: 
                  max = dict[x]
                  maxElt = x
            else: 
               dict[x] = 0
         return maxElt
      
#https://leetcode.com/problems/majority-element/
#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.