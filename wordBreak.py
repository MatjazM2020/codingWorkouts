from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        
        dp = [False]*(l+1)
        dp[0] = True
        for i in range(1,l+1):
            for j in range(i):  
                if dp[j] and s[j:i] in wordDict: 
                    dp[i] = True
                    break; 
        return dp[l]
        


#https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=dynamic-programming
#Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
# sequence of one or more dictionary words.Note that the same word in the dictionary may be reused multiple times in the segmentation.