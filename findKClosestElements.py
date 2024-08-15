from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        while l < r:
            c = l + (r - l)//2
            if arr[c] > x:
                r = c
            elif arr[c] < x:
                l = c + 1
            else:
                l = c
                break

        l, r = l-1, l
        n = len(arr)
        while k > 0:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l]-x) <= abs(arr[r]-x):
                l -= 1
            else:
                r += 1
            k -= 1
        return arr[l+1:r]
    
    
'''
https://leetcode.com/problems/find-k-closest-elements/description/?envType=study-plan-v2&envId=binary-search

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

'''