class Solution:
    def findLongestChain(self, pairs):
        n = len(pairs)
        dp = [1 for _ in range(n)]
        
        pairs = sorted(pairs, key = lambda x: x[1])
        
        for i in range(n): 
            for j in range(i): 
                if pairs[i][0] > pairs[j][1]: 
                    dp[i] = max(1+dp[j], dp[i])
        return max(dp)

#https://leetcode.com/problems/maximum-length-of-pair-chain/?envType=study-plan-v2&envId=dynamic-programming
#You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
#A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
#Return the length longest chain which can be formed.
#You do not need to use up all the given intervals. You can select pairs in any order.