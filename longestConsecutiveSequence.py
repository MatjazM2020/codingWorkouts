from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elts = set(nums)
        res = 0
        for x in elts:
            if x-1 not in elts:
                curr = x
                seqLen = 1

                while curr+1 in elts:
                    curr += 1
                    seqLen += 1
                if seqLen > res:
                    res = seqLen
        return res


'''
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''