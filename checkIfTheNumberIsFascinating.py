class Solution:
    def isFascinating(self, n: int) -> bool:
        string = str(n) + str(2*n) + str(3*n)
        chrs = set(string)
        if '0' not in chrs and len(chrs) == 9 and len(string) == 9: return True
        return False
    
   
    
'''
https://leetcode.com/problems/check-if-the-number-is-fascinating/description/

You are given an integer n that consists of exactly 3 digits.

We call the number n fascinating if, after the following modification, the resulting number 
contains all the digits from 1 to 9 exactly once and does not contain any 0's:

Concatenate n with the numbers 2 * n and 3 * n.
Return true if n is fascinating, or false otherwise.

Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.



'''