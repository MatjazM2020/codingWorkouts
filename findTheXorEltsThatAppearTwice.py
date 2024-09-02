from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen, res = set(), 0
        for elt in nums:
            if elt not in seen:
                seen.add(elt)
            else:
                res ^= elt
        return res
    
'''
https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/

You are given an array nums, where each number in the array appears either once or twice.

Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.

'''
