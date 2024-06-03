from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        
        valids = {str(i) for i in range(1,27)}
        
        def valid(chunk: str) -> bool:
            return (chunk in valids)

        @cache
        def helper(st: str) -> int: 
            if not st:
                return 1
            if st[0] == '0':
                return 0
            cnt = 0
            if valid(st[:1]):
                cnt += helper(st[1:]) 
            if len(st) >= 2 and valid(st[:2]):
                cnt += helper(st[2:])
            return cnt
        return helper(s)


'''
https://leetcode.com/problems/decode-ways/?envType=study-plan-v2&envId=dynamic-programming
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.
'''