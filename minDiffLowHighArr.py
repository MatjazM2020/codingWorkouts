from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        min_diff = float('inf')
        
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            min_diff = min_diff if min_diff < diff else diff
        
        return min_diff


'''
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.
'''