class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        numOfInts = 0
        for i in range(low, high+1): 
            x = str(i)
            sum1 = 0
            sum2 = 0
            if len(x)%2 == 0: 
                for j in range(len(x)//2): 
                    sum1 += int(x[j])
                for j in range(len(x)//2, len(x)): 
                    sum2 += int(x[j])
                if sum1 == sum2: 
                    numOfInts += 1 
        return numOfInts
        
        
        
        
# Exercise: https://leetcode.com/problems/count-symmetric-integers/
#You are given two positive integers low and high. An integer x consisting of 2 * n digits is symmetric if the sum
# of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are
# never symmetric. Return the number of symmetric integers in the range [low, high].