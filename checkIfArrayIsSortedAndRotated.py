from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        rotPoint, n = 0, len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                rotPoint += 1
            if rotPoint > 1:
                return False
        return True
    
    
    
'''
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some
number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length],
where % is the modulo operation.



'''