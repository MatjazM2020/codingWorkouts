from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        x = 0
        for i in range(len(s)//2): 
            x = s[len(s)-i-1]
            s[len(s)-i-1] = s[i]
            s[i] = x
                    
#https://leetcode.com/problems/reverse-string/
#Write a function that reverses a string. The input string is given as an array of characters s.
