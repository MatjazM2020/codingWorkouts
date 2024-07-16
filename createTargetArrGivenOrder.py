from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        x = []
        for i in range(len(nums)): 
            x.insert(index[i],nums[i])
        return x
    
    
    
    
'''
https://leetcode.com/problems/create-target-array-in-the-given-order/description/


Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.
'''
