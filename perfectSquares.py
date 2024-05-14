from functools import cache
from math import sqrt
class Solution:
    @cache
    def numSquares(self, n: int) -> int:
        if (sqrt(n) - int(sqrt(n)) == 0): 
            return 1 
        else: 
            minim = 9999999999
            for i in range(1,int(sqrt(n)) + 1):
                    minim = min(minim, self.numSquares(n-(i*i)))
            return minim + 1



# https://leetcode.com/problems/perfect-squares/description/?envType=study-plan-v2&envId=dynamic-programming
# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.