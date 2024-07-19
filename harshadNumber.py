class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x_str = str(x)
        dig_sum = 0
        for i in x_str:
            dig_sum += int(i)
        if x%dig_sum == 0:
            return dig_sum
        return -1
    
    
    
    
'''
https://leetcode.com/problems/harshad-number/description/

An integer divisible by the sum of its digits is said to be a Harshad number.
You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.
'''