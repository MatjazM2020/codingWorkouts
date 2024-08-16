from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)-1
        nums.sort()
        count = 0
        for i in range(n, 0, -1):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count
    
    
    
'''
https://leetcode.com/problems/valid-triangle-number/description/?envType=study-plan-v2&envId=binary-search

Given an integer array nums, return the number of triplets chosen from the array that can make
triangles if we take them as side lengths of a triangle.

'''