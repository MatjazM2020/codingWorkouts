from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dict = {}
        for w in words:
            if w not in dict:
                dict[w] = 1
            else:
                dict[w] += 1
        res = 0
        mid = False
        wordSet = set(words)
        for w in wordSet:
            if w[0] == w[1]:
                if dict[w] > 1:
                    if dict[w]%2 == 0:
                        res += dict[w]*2
                    else:
                        res += (dict[w]-1)*2
                        if not mid:
                            res += 2
                            mid = True
                else:
                    if not mid:
                        res += 2
                        mid = True
            elif w[::-1] in dict:
                res += min(dict[w[::-1]], dict[w])*2
        return res
    
    
    
'''
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating 
them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create
any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.
'''