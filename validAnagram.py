class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
      dict1 = {}
      dict2 = {}
      if len(s) == 1 and len(t) == 1 and s == t:
         return True
      for c in s: 
         if c in dict1:
            dict1[c] += 1
         else: 
            dict1[c] = 1
      for c in t: 
         if c in dict2:
            dict2[c] += 1
         else: 
            dict2[c] = 1
      if dict1 == dict2: 
         return True
      else:
         return False



#https://leetcode.com/problems/valid-anagram/
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.
