from functools import cache

class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n < 2: 
            return 1
        sx = 0
        for i in range(1,n+1): 
            sx += self.numTrees(i-1) * self.numTrees(n-i) 
        return sx
    
      
# https://leetcode.com/problems/unique-binary-search-trees/description/?envType=study-plan-v2&envId=dynamic-programming
̧# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

