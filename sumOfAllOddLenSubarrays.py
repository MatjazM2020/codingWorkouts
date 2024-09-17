from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n, res = len(arr), 0
        for i in range(1, n+1, 2):
            for j in range(n-i+1):
                print(arr[j:j+i])
                res += sum(arr[j:j+i])
        return res


'''
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.
'''
