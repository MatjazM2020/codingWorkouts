class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: 
            return 0 
        
        dp = [0 for _ in range(n)]
        dp[1] = max(prices[1]-prices[0], 0)
                
        for i in range(2, n): 
            mx = -99999999999
            for j in range(i):
                if j > 1: 
                    temp = dp[j-2] + (prices[i] - prices[j])
                elif j == 0:
                    temp = (prices[i] - prices[j])
                elif j == 1: 
                    temp = dp[j-1] + (prices[i] - prices[j])
                if temp > mx: 
                    mx = temp
            dp[i] = max(dp[i-1], mx)
        return dp[n-1]
    
    
    
    
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/?envType=study-plan-v2&envId=dynamic-programming
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like 
# (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).