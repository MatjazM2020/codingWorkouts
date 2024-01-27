class Solution(object):
    def minDelSum(self, s1, s2, memo): 
        if (s1,s2) in memo: 
            return memo[(s1,s2)]
        if not s1 and not s2: 
            return 0
        elif not s1: 
            sm = 0
            for x in s2: 
                sm += ord(x)
            memo[(s1,s2)] = sm
            return memo[(s1,s2)]
        elif not s2: 
            sm = 0
            for x in s1: 
                sm += ord(x)
            memo[(s1,s2)] = sm
            return memo[(s1,s2)]
        elif s1[0] == s2[0]:
            memo[(s1,s2)] = self.minDelSum(s1[1:],s2[1:],memo) 
            return memo[(s1,s2)]
        else: 
            memo[(s1,s2)] = min(ord(s2[0])+self.minDelSum(s1,s2[1:],memo),ord(s1[0])+self.minDelSum(s1[1:],s2,memo))
            return memo[(s1,s2)]
    def minimumDeleteSum(self, s1, s2):
        return self.minDelSum(s1,s2,{})
    
    
#https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/?envType=study-plan-v2&envId=dynamic-programming
#Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.