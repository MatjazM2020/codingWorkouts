from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        ref = nums[0]
        if ref < nums[-1]:
            return ref
        l, r, cap = 1, len(nums)-1, nums[0]
        while l <= r:
            c = (l+r)//2
            if nums[c] > ref:
                l = c + 1
            elif nums[c] < ref:
                cap = nums[c]
                r = c - 1
        return cap
    
    
    
'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=binary-search

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

'''