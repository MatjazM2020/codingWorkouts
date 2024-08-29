from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n, smallest = len(nums), float('inf')
        nums.sort()
        for i in range(n//2):
            tmp = (nums[i]+nums[n-i-1])/2
            if tmp < smallest:
                smallest = tmp
        return smallest
    
    
'''
https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/

You have an array of floating point numbers averages which is initially empty. 
You are given an array nums of n integers where n is even.

You repeat the following procedure n / 2 times:

Remove the smallest element, minElement, and the largest element maxElement, from nums.
Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages.

'''