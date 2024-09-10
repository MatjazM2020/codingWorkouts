from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ordered = [(i, nums[i]) for i in range(n)]
        ordered.sort(key=lambda x: x[1])

        res = [0 for _ in range(n)]
        for i in range(1,n):
            if ordered[i][1] == ordered[i-1][1]:
                res[ordered[i][0]] = res[ordered[i-1][0]]
            else: 
                res[ordered[i][0]] = i
        return res
    
    
    
'''
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''