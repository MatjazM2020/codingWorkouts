from functools import cache

class Solution:
    @cache 
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        i = 0 
        j = n-1
        if i == j: 
            return 1
        elif j<i: 
            return 0 
        elif s[i] == s[j]: 
            return 2 + self.longestPalindromeSubseq(s[i+1:j]) 
        else: 
            return max(self.longestPalindromeSubseq(s[i+1:j+1]),self.longestPalindromeSubseq(s[i:j]))



#https://leetcode.com/problems/longest-palindromic-subsequence/description/?envType=study-plan-v2&envId=dynamic-programming
#Given a string s, find the longest palindromic subsequence's length in s.
#A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without 
# changing the order of the remaining elements.

