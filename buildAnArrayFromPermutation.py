from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = len(nums)*[0]
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
    
    
'''
https://leetcode.com/problems/build-array-from-permutation/description/

Given a zero-based permutation nums (0-indexed), build an array ans of the same 
length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

'''