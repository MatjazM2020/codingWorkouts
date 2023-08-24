from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        for i in range(len(nums)):
            dict = {}       
            dict[nums[i]] = 1
            for j in range(i+1, min(len(nums), i+1+k)):
               try:
                 dict[nums[j]] += 1
                 if dict[nums[j]] == 2:
                    return True
               except: 
                dict[nums[j]] = 1
        return False
        

#https://leetcode.com/problems/contains-duplicate-ii/
#Given an integer array nums and an integer k, return true if there are two distinct
# indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.