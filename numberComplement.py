class Solution:
    def findComplement(self, num: int) -> int:
        x = bin(num)[2:]
        for i in range(len(x)): 
          if x[i] == '0': 
            x = x[:i]+'1'+x[i+1:]
          else: 
            x = x[:i]+'0'+x[i+1:]
        return int(x,2)

      
#https://leetcode.com/problems/number-complement/
#The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's 
# in its binary representation. For example, The integer 5 is "101" in binary and its complement is "010" which
# is the integer 2. Given an integer num, return its complement.