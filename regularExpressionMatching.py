from functools import cache


class Solution:
    @cache
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        elif not p and s:
            return False
        elif p[-1] == '*':
            if not s:
                return self.isMatch(s, p[:-2])
            if p[-2] == '.':
                return self.isMatch(s, p[:-2]) or self.isMatch(s[:-1], p)
            else:
                if s[-1] == p[-2]:
                    return self.isMatch(s[:-1], p) or self.isMatch(s, p[:-2]) 
                else:
                    return self.isMatch(s, p[:-2])
        elif p[-1] == '.':
            if not s:
                return False
            return self.isMatch(s[:-1], p[:-1])
        elif not s:
            return False
        elif p[-1] == s[-1]:
                return self.isMatch(s[:-1], p[:-1])
        return False



'''
https://leetcode.com/problems/regular-expression-matching/description/

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

'''