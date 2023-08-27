class Solution:    
    def helper(self, s: str, a: int) -> str: 
     for i in range(len(s)): 
        if i >= len(s):
            break
        if s[i].isupper():
            s = s[:i]+s[i].lower()+s[i+1:]
        while not(s[i].isupper()) and not(s[i].islower()) and not(s[i].isnumeric()): 
            s = s[:i]+s[i+1:]
            if i == len(s) or s == '':
                break
            if s[i].isupper(): 
                s = s[:i]+s[i].lower()+s[i+1:]
     return s
            
    def isPalindrome(self, s: str) -> bool:
        s = self.helper(s, 0)
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
                

        
#https://leetcode.com/problems/valid-palindrome/
#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
# characters include letters and numbers.Given a string s, return true if it is a palindrome, or false otherwise.

