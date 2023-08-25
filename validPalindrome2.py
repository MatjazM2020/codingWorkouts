from typing import List

class Solution:
    def validPalindrome(self, s: str) -> bool:
        str1 = ''
        str2 = ''
        b1 = True
        b2 = True
        for i in range(len(s)): 
            if s[i] != s[len(s)-1-i]:
                str1 = s[:i]+s[i+1:]
                str2 = s[:len(s)-1-i]+s[len(s)-1-i+1:]
        for i in range(len(str1)): 
            if str1[i] != str1[len(str1)-1-i]:
                b1 = False
        for i in range(len(str2)):
            if str2[i] != str2[len(str2)-1-i]:
                b2 = False
        return b1 or b2
   
#https://leetcode.com/problems/valid-palindrome-ii/submissions/
#Given a string s, return true if the s can be palindrome after deleting at most one character from it.