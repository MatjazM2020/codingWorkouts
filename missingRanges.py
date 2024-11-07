from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if nums == []: return [[lower, upper]]
        res = []
        if lower < nums[0]: 
            res.append([lower, nums[0]-1])
        i = 0
        
        while i < len(nums) - 1 and nums[i] < upper:
            if nums[i] < nums[i+1] - 1:
                res.append([nums[i]+1, nums[i+1]-1])
            i += 1
        if upper > nums[-1]: 
            res.append([nums[-1]+1, upper])
        
        return res



'''
https://leetcode.com/problems/missing-ranges/

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of
the ranges, and each missing number is covered by one of the ranges.

'''