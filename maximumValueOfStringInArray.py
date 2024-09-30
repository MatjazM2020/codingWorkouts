
from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res,t,  nums = 0, False, {'0','1','2','3','4','5','6','7','8','9'}
        for s in strs:
            t = False
            for c in s:
                if c not in nums:
                    t = True
            if not t: res = max(res, int(s))
            else: res = max(res, len(s))
        return res
                
'''
https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

The value of an alphanumeric string can be defined as:

The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
'''
