from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def isPalindrome(word):
            l = len(word)//2
            while l >= 0:
                if word[l] != word[-l-1]:
                    return False
                    break
                l -= 1
            return True
        for w in words:
            if isPalindrome(w):
                return w
        return ''
    
    
    
'''
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

Given an array of strings words, return the first palindromic string in the array.
If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
'''



