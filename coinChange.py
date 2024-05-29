from functools import cache
from typing import List
import sys 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        inf = sys.maxsize
        dp = [inf for _ in range(amount+1)]
        dp[0] = 0
        
        for i in range(1, amount+1):
            minX = inf
            for x in coins: 
                if i >= x:
                    minX = min(minX, dp[i-x]+1)
            dp[i] = minX
        return dp[n] if dp[n] != inf else -1


'''
https://leetcode.com/problems/coin-change/description/?envType=study-plan-v2&envId=dynamic-programming
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
'''


