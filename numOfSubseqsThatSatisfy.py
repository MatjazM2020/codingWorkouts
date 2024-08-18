from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = (10**9) + 7
        def numSubsequences(k: int) -> int:
            return pow(2, k, mod)
        n = len(nums) - 1
        nums.sort()
        count = 0
        l, r = 0, n
        while l <= r:
            if nums[l] + nums[r] <= target:
                count = (count +numSubsequences(r-l))%mod
                l += 1
            else:
                r -= 1
        return count 
    
    
'''
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/?envType=study-plan-v2&envId=binary-search
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum
element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

'''