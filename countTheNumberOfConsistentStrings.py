from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for x in words:
            if set(x).issubset(allowed): count += 1
        return count
    
    
    
'''
https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

'''