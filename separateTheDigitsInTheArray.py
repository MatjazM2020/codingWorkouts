from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return map(int, list(''.join(map(str, nums))))
    
    
    
'''
https://leetcode.com/problems/separate-the-digits-in-an-array/description/

Given an array of positive integers nums, return an array answer that consists of the 
digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
'''