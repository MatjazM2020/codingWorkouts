from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = -1
        count = 0
        for x in nums: 
            if x == 1:
                count += 1
            else: 
                if count > max: 
                    max = count
                count = 0
        if count > max:
            return count
        return max
        
#https://leetcode.com/problems/max-consecutive-ones/
#Given a binary array nums, return the maximum number of consecutive 1's in the array.