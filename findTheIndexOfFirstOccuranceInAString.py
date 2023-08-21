class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       s = 0
       if len(needle) <= len(haystack): 
           for i in range(len(haystack)-len(needle)+1): 
              s = 0
              for j in range(len(needle)): 
                if haystack[i+j] == needle[j]: 
                   s+=1
                else: 
                   s = 0
                if s == len(needle): 
                    return i
       return -1

#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#Given two strings needle and haystack, return the index of the first occurrence of
# needle in haystack, or -1 if needle is not part of haystack.