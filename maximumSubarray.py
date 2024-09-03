from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, curr_max, max_global = len(nums), nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_max = max(nums[i], nums[i] + curr_max)
            if curr_max > max_global:
                max_global = curr_max
        return max_global
    
    
'''
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the subarray
 with the largest sum, and return its sum.

'''