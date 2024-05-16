from functools import cache
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def helper(tar: int):
            if tar < 0:
                return 0 
            elif tar == 0: 
                return 1 
            accum = 0
            for j in range(n):
                accum += helper(tar-nums[j])            
            return accum
        return helper(target)
    


#https://leetcode.com/problems/combination-sum-iv/?envType=study-plan-v2&envId=dynamic-programming
#Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
#The test cases are generated so that the answer can fit in a 32-bit integer.