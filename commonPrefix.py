from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        x = strs.__getitem__(0)
        if len(x) == 0:
            return ''
        
        for i in range(len(strs)-1): 
            y = strs.__getitem__(i+1)
            if len(y) == 0: 
                return ''
            conc = ''
            
            if len(y) < len(x): 
                lght = len(y)
            else: 
                lght = len(x)

            for j in range(lght): 
                if x[j] == y[j]:
                    conc = conc + x[j]
                else:
                    break
            x = conc
        return x
    

#Exercise: https://leetcode.com/problems/longest-common-prefix/
#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

