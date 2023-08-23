class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n%2 == 0:  
            return self.isPowerOfTwo(n//2)
        else: 
            return False
        
        
#https://leetcode.com/problems/power-of-two/
#Given an integer n, return true if it is a power of two. Otherwise, return false.