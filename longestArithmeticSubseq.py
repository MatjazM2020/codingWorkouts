class Solution:
    def longestSubsequence(self, arr, difference):
        
        dp = {}
        maxL = 1 
        for x in arr: 
            if (x - difference) in dp: 
                dp[x] = dp[x-difference]+1
                maxL = max(maxL, dp[x])
            else:
                dp[x] = 1
        return maxL
    
    
    
    
#https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/?envType=study-plan-v2&envId=dynamic-programming
#Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic
# sequence such that the difference between adjacent elements in the subsequence equals difference.