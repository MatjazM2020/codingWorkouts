class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        res = 0
        if len(x) < len(y): 
            for i in range(len(y)-len(x)): 
                x = '0'+x
        elif len(x) > len(y): 
            for i in range(len(x)-len(y)): 
                y = '0'+ y 
        for i in range(max(len(x),len(y))): 
            if x[i] != y[i]: 
                res += 1
        return res
                
        
        
#https://leetcode.com/problems/hamming-distance/
#The Hamming distance between two integers is the number of positions at which the 
# corresponding bits are different. Given two integers x and y, return the Hamming distance between them.