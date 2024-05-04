class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        if n == 1: 
            return 0     

        minPrice = prices[0]
        accum = 0
        
        for i in range(1,n):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] > minPrice + fee:
                accum += prices[i] - minPrice - fee 
                minPrice = prices[i] - fee

        return accum
  
  
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/?envType=study-plan-v2&envId=dynamic-programming  
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# Note:
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.
