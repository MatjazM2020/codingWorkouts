from typing import List
import copy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
           k = k % len(nums)
        arr2 = copy.deepcopy(nums)
        for i in range(len(nums)): 
            arr2[(i+k)%len(nums)] = nums[i]
        for i in range(len(nums)): 
            nums[i] = arr2[i]
               
#https://leetcode.com/problems/rotate-array/
#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.