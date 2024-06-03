from functools import cache

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        modulus = 10**9 + 7
        @cache
        def helper(size: int) -> int: 
            if size == 0: 
                return 1
            elif size < 0: 
                return 0
            return (helper(size-zero) + helper(size-one)) % modulus
        acc = 0
        for x in range(low, high+1):
            acc = (acc + helper(x)) % modulus
        return acc % modulus




'''
https://leetcode.com/problems/count-ways-to-build-good-strings/description/?envType=study-plan-v2&envId=dynamic-programming
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at 
each step perform either of the following:
Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.
A good string is a string constructed by the above process having a length between low and high (inclusive).
Return the number of different good strings that can be constructed satisfying these properties.
Since the answer can be large, return it modulo 109 + 7.
'''