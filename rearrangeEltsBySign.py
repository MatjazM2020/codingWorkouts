from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        res = []
        for i in range(len(neg)):
            res.append(pos[i])
            res.append(neg[i])
        return res
    
    
'''
https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

You are given a 0-indexed integer array nums of even length consisting of an equal number of
positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions
'''