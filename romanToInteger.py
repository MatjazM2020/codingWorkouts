import numpy 
class Solution:
    def romanToInt(self, s: str) -> int:
        a = numpy.empty(len(s), dtype=int )
        for i in range(len(s)): 
            match s[i]: 
                case 'I':
                    a[i] = 1
                case 'V':
                    a[i] = 5
                case 'X': 
                    a[i] = 10
                case 'L':
                    a[i] = 50
                case 'C': 
                    a[i] = 100
                case 'D':
                    a[i] = 500
                case 'M':
                    a[i] = 1000
        num = 0
        for i in range(len(s)-1): 
            if a[i] >= a[i+1] and a[i] != 1001: 
                num += a[i]
            elif a[i] != 1001:
                num += a[i+1] - a[i]
                a[i+1] = 1001
        if a[len(s)-1] != 1001:
            num += a[len(s)-1]
        return num

            
        
instance = Solution()
print(instance.romanToInt("IX"))
        
        
        
        
        
#Excercise: https://leetcode.com/problems/roman-to-integer/        
#Roman numerals are usually written largest to smallest from left to right. However, 
#the numeral for four is not IIII. Instead, the number four is written as IV. 
#Because the one is before the five we subtract it making four. 
#The same principle applies to the number nine, which is written
#as IX. There are six instances where subtraction is used:
#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer