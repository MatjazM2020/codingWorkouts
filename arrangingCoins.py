class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1 or n== 2:
            return 1
        sum = 0
        for i in range(n): 
            sum += i
            if sum > n: 
                return i-1
            elif sum == n:
                return i
            
# exercise: https://leetcode.com/problems/arranging-coins/
#You have n coins and you want to build a staircase with these coins. The staircase consists of k rows
# where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

