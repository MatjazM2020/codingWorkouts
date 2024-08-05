from typing import List 


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        def findRotator():
            ref = nums[0]
            if ref < nums[-1]:
                return len(nums)-1
            l, r = 1, len(nums)-1
            while l <= r: 
                c = (l+r)//2
                if nums[c] < ref:
                    r = c - 1
                elif nums[c] > ref: 
                    l = c + 1
                else:
                    return c
            return c
        
        def binSearch(i, j):
            l, r, c = i, j, 0
            while l <= r: 
                c = (l+r)//2
                if nums[c] > target:
                    r = c - 1
                elif nums[c] < target:
                    l = c + 1
                else:
                    return c
            return -1
        
        mid = findRotator()
        at1 = binSearch(0, mid)
        at2 = binSearch(mid, len(nums)-1)
        
        if at1 != -1:
            return at1
        return at2
        
        
        
        
    
    
'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=binary-search

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that 
the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example
, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1
if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

'''