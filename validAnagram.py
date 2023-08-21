class Solution:
   dict1 = {}
   dict2 = {}
   def isAnagram(self, s: str, t: str) -> bool:
      for c in s: 
         if c in self.dict1:
            self.dict1[c] += 1
         else: 
            self.dict1[c] = 0
      for c in t: 
         if c in self.dict2:
            self.dict2[c] += 1
         else: 
            self.dict2[c] = 0
      if self.dict1 == self.dict2: 
         return True
      return False




#https://leetcode.com/problems/valid-anagram/
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.