class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ls = date.split('-')
        return bin(int(ls[0]))[2:] + '-' + bin(int(ls[1]))[2:] + '-' + bin(int(ls[2]))[2:]
    
    
   
    
'''
https://leetcode.com/problems/convert-date-to-binary/description/

You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

date can be written in its binary representation obtained by converting year, month, and day to 
their binary representations without any leading zeroes and writing them down in year-month-day format.

Return the binary representation of date.

'''