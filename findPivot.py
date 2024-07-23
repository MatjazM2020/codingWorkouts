from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        right = sum(nums)-nums[0]
        if right == 0:
            return 0
        left = 0
        for i in range(1,n):
            right -= nums[i]
            left += nums[i-1]
            if right == left:
                return(i)
        return(-1)
    



'''
https://leetcode.com/problems/find-pivot-index/
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
'''