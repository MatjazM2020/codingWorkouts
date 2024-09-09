from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen, once, sumUp = set(), set(), 0
        for x in nums:
            if x in seen:
                once.discard(x)
            else:
                seen.add(x)
                once.add(x)
        return sum(once)
    
'''
https://leetcode.com/problems/sum-of-unique-elements/description/

You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
'''