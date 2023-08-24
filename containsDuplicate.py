from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for x in nums:
            try:
                dict[x] += 1
                if dict[x] == 2:
                    return True
            except: 
                dict[x] = 1
        return False
            

#https://leetcode.com/problems/contains-duplicate/
#Given an integer array nums, return true if any value appears at least twice in 
# the array, and return false if every element is distinct.