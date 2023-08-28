class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0: 
            return False
        elif n == 1: 
            return True
        elif n%3 == 0: 
            return self.isPowerOfThree(n//3)
        else: 
            return False
            
        
               
#https://leetcode.com/problems/power-of-three/
#Given an integer n, return true if it is a power of three. Otherwise, return false.
#An integer n is a power of three, if there exists an integer x such that n == 3x.