class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] == nums[j] and i < j: 
                    count += 1
        return count
    
    
    
    
#https://leetcode.com/problems/number-of-good-pairs/
#Given an array of integers nums, return the number of good pairs.
#A pair (i, j) is called good if nums[i] == nums[j] and i < j.