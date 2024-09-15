from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxElt, n, currLen, maxLen = max(nums), len(nums), 0, 0
        for i in range(n):
            if nums[i] == maxElt:
                currLen += 1
                if maxLen < currLen:
                    maxLen = currLen
            else:
                currLen = 0
        return maxLen
    


'''
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/

You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. 
Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.

'''