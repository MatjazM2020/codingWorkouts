class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        res = 0
        i = 0
        l, r = 0,0
        while i < n: 
            if s[i] == 'L':
                l += 1
            else: 
                r += 1
            if l == r:
                l, r = 0,0 
                res += 1
            i += 1
        return res
    

'''
https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.
'''