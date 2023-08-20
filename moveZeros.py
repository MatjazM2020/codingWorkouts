from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for j in range(len(nums)): 
         if nums[j] == 0: 
            a = j
            indx = j
            if indx != len(nums): 
             while nums[indx] == 0 and indx != len(nums)-1:
                 indx += 1
             if indx != len(nums): 
                 nums[a] = nums[indx]
                 nums[indx] = 0

#Exercise: https://leetcode.com/problems/move-zeroes/
#Given an integer array nums, move all 0's to the end of it while maintaining
#the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.
