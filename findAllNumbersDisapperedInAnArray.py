from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = set(nums)
        diss = []
        for i in range(1,len(nums)+1): 
            if not(i in x): 
                diss.append(i)
        return diss
        
        
        

#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
#Given an array nums of n integers where nums[i] is in the range [1, n], return an 
# array of all the integers in the range [1, n] that do not appear in nums.