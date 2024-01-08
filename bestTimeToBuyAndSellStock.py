class Solution(object):
    def maxProfit(self, prices):
        maxx = 0 
        minn = 999999
        for i in range(len(prices)): 
            if prices[i] < minn: 
                minn = prices[i]
            if prices[i]-minn > maxx: 
                maxx = prices[i]-minn
        return maxx 




            
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in 
# the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot 
# achieve any profit, return 0.