from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r= 0, len(nums)-1
        if nums[l] < nums[r] or r == 0:
            return nums[l]

        while l <= r:
            c = l + (r-l)//2
            if nums[r] > nums[c]:
                r = c
            elif nums[r] < nums[c]:
                l = c + 1 
            else:
                r -= 1
        return nums[l]
    
    
    
    
'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/?envType=study-plan-v2&envId=binary-search

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

'''