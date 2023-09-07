from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
      res = []
      set1 = {'q','w','e','r','t','y','u','i','o','p'}
      set2 = {'a','s','d','f','g','h','j','k','l'}
      set3 = {'z','x','c','v','b','n','m'}
      tf = True
      for x in words:
        if x[0].upper() in set1 or x[0].lower() in set1: 
          belongs = set1
        elif x[0].upper() in set2 or x[0].lower() in set2: 
          belongs = set2
        else:
          belongs = set3          
        for i in range(1,len(x)): 
          if not(x[i].upper() in belongs or x[i].lower() in belongs):
            tf = False
            break
        if tf == True: 
          res.append(x)
        tf = True
      return res
        


#https://leetcode.com/problems/keyboard-row/
#Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row 
# of American keyboard like the image below. In the American keyboard:
#the first row consists of the characters "qwertyuiop",
#the second row consists of the characters "asdfghjkl", and
#the third row consists of the characters "zxcvbnm".