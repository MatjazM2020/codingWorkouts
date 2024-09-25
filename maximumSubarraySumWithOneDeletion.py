from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(n)
        max_ends = [0]*n
        max_ends[0] = arr[0]
        for i in range(1, n):
            max_ends[i] = max(max_ends[i-1]+arr[i], arr[i])
        
        max_ends_neg = [0]*n
        max_ends_neg[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            max_ends_neg[i] = max(max_ends_neg[i+1]+arr[i], arr[i])
        
        max_no_deletions = max(max_ends)
        for i in range(1, n-1):
            max_no_deletions = max(max_no_deletions, max_ends[i-1]+ max_ends_neg[i+1])
        return max_no_deletions
        
        
        
        
        


'''
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/

Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements)
with at most one element deletion. In other words, you want to choose a subarray and optionally delete one
element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.
'''
