class Solution(object):
    def wordPattern(self, pattern, s):
        dict = {}
        ls = split(s)
        i = 0
        if len(set(pattern)) != len(set(ls)) or len(pattern) != len(ls): 
            return False
        for x in pattern: 
            if x not in dict: 
                dict[x] = ls[i]
                i += 1
            elif dict[x] != ls[i]:
                return False
            else:
                i += 1
        return True




#https://leetcode.com/problems/word-pattern/description/
#Given a pattern and a string s, find if s follows the same pattern.
#Here follow means a full match, such that there is a bijection between a 
# letter in pattern and a non-empty word in s.

