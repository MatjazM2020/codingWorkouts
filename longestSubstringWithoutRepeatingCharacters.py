class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 1 
        maxL = 1 
        cur = 0
        for l in range(len(s)): 
            while r < len(s) and not(s[r] in s[l:r]):
                cur = r-l+1
                if cur > maxL: 
                   maxL = cur  
                r += 1
        return min(maxL, len(s)) 
    
    
    
    
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#Given a string s, find the length of the longest substring without repeating characters.

