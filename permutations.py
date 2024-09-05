import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)
    
'''
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


'''