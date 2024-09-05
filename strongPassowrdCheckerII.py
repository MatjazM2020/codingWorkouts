class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n, special_chars = len(password), "!@#$%^&*()-+"
        if n < 8: return False
        
        checks = [False for _ in range(4)]
        for i in range(n):
            if password[i].islower():
                checks[0] = True
            if password[i].isupper():
                checks[1] = True
            if password[i].isdigit():
                checks[2] = True
            if password[i] in special_chars:
                checks[3] = True
            if i < n-1 and password[i] == password[i+1]:
                return False
        return all(checks)
    
    
'''
https://leetcode.com/problems/strong-password-checker-ii/description/

A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters
in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates
this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.

'''