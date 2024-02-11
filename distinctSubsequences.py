class Solution(object):
    def numDist(self, s, t, d): 
        if (s,t) in d:
            return d[(s,t)]
        if len(s) < len(t): 
            return 0 
        if not t:
            return 1
        if not s: 
            return 0 
        if s[0] == t[0]: 
            d[(s,t)] = self.numDist(s[1:],t[1:],d)+self.numDist(s[1:], t,d)
            return d[(s,t)]
        else:
            d[(s,t)] = self.numDist(s[1:],t,d)
            return d[(s,t)]
    def numDistinct(self, s, t):
        return self.numDist(s,t,{})
        



#https://leetcode.com/problems/distinct-subsequences/description/?envType=study-plan-v2&envId=dynamic-programming
#Given two strings s and t, return the number of distinct subsequences of s which equals t.
#The test cases are generated so that the answer fits on a 32-bit signed integer.