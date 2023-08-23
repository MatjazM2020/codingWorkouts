class Solution:
    def hammingWeight(self, n: int) -> int:
        x = str(bin(n))
        count = 0
        for a in x:
            if a == '1':
                count += 1
        return count




#https://leetcode.com/problems/number-of-1-bits/
#Write a function that takes the binary representation of an unsigned integer and returns the 
# number of '1' bits it has (also known as the Hamming weight).
