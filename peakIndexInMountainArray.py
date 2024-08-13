from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l, r = 0, len(arr)-2

        while l<= r:
            c = l + (r-l)//2
            if arr[c] > arr[c+1]:
                r = c - 1 
            elif arr[c] < arr[c+1]:
                l = c + 1
            else:
                return c
        return l
    
    
'''
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/?envType=study-plan-v2&envId=binary-search

You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.
'''