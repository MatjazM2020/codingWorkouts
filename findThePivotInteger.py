class Solution:
    def pivotInteger(self, n: int) -> int:
        smRight, smLeft = sum(range(n+1)), 0
        for i in range(1,n+1):
            smLeft += i
            smRight -= i-1
            if smLeft == smRight:
                return i
        return -1
    
    
    
    
'''
https://leetcode.com/problems/find-the-pivot-integer/description/

Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum
of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. 
It is guaranteed that there will be at most one pivot index for the given input.

'''