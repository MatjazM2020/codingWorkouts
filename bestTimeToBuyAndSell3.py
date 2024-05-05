class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: 
            return 0 

        forwardProfit = [0 for _ in range(n)]
        minPrice = prices[0]
        mx = 0

        for i in range(1,n): 
            minPrice = min(prices[i], minPrice)
            mx = max(mx, prices[i]-minPrice)
            forwardProfit[i] = mx

        backwardProfit = [0 for _ in range(n)]
        maxPrice = prices[-1]
        mx = 0

        for i in range(n-2, -1, -1):
            maxPrice = max(prices[i], maxPrice)
            mx = max(mx, maxPrice - prices[i])
            backwardProfit[i] = mx


        maxProfit = 0
        for i in range(n):
            maxProfit = max(maxProfit, backwardProfit[i] + forwardProfit[i])
        return maxProfit





#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/?envType=study-plan-v2&envId=dynamic-programming
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

