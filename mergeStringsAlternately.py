class Solution:
    def mergeHelper(self, word: str, word1: str, word2: str, i: int, j: int) -> str:
        if i== len(word1) and j == len(word2): 
            return word
        elif i == len(word1):
            word += word2[j:]
            return word
        elif j ==len(word2):
            word += word1[i:]
            return word
        else: 
            if (i+j)%2 == 0:
                word += word1[i]
                return self.mergeHelper(word,word1,word2,i+1,j)
            else:
                word += word2[j]
                return self.mergeHelper(word,word1,word2,i,j+1)
            
            
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return self.mergeHelper('',word1,word2,0,0)



#Exercise: https://leetcode.com/problems/merge-strings-alternately/
#You are given two strings word1 and word2. Merge the strings by adding letters 
# in alternating order, starting with word1. If a string is longer than the other, 
# append the additional letters onto the end of the merged string.
#Return the merged string.

        
        
        
        
        
        
        
#Exercise: https://leetcode.com/problems/merge-strings-alternately/
#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto 
# the end of the merged string.
#Return the merged string.