class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict1, dict2, res  = dict(),dict(), 0
        for x in s:
            if x in dict1:
                dict1[x] += 1
            else:
                dict1[x] = 1
        for x in t:
            if x in dict2:
                dict2[x] += 1
            else:
                dict2[x] = 1
        
        for x in dict1:
            if dict1[x] > dict2.get(x, 0):
                res += dict1[x]-dict2.get(x, 0)

        return res
    
'''
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.    
'''