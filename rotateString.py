class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        k = s
        for i in range(len(s)): 
            k = k[1:]+k[0]
            if k == goal:
                return True
        return False
    
        
        
        
#problem: https://leetcode.com/problems/rotate-string/
#Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
#A shift on s consists of moving the leftmost character of s to the rightmost position.
#For example, if s = "abcde", then it will be "bcdea" after one shift.