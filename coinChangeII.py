from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def helper(amt: int, i: int):
            if amt == 0: 
                return 1
            elif amt < 0: 
                return 0

            accum = 0
            for j in range(i, n): 
                accum += helper(amt - coins[j], j)
            return accum
        return helper(amount, 0)
    
    



# https://leetcode.com/problems/coin-change-ii/description/?envType=study-plan-v2&envId=dynamic-programming
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.