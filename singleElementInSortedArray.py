from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        l, r, cap, n = 0, len(nums)-1, 0, len(nums)
        while l<= r:
            c = l + (r-l)//2
            i = 1 if c%2 == 0 else -1
            if (c+i < n and c+i >= 0) and nums[c] == nums[c+i]:
                l = c + 1
            else:
                cap = c
                r = c - 1
        return nums[cap]





'''
https://leetcode.com/problems/single-element-in-a-sorted-array/description/?envType=study-plan-v2&envId=binary-search

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

'''