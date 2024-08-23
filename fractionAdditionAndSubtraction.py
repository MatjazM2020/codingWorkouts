from fractions import Fraction
import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        l = re.split(r'(\+|\-)', expression)
        n = len(l)
        acc = 0
        for i in range(0, n, 2):
            if l[i] == '':
                continue
            if i == 0:
                acc += Fraction(l[0])
            else:
                acc += Fraction(l[i-1] + l[i])
        res = str(acc)+'/1' if acc.denominator == 1 else str(acc)
        return res
    
    
    

'''
https://leetcode.com/problems/fraction-addition-and-subtraction/description/?envType=daily-question&envId=2024-08-23

Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction
that has a denominator 1. So in this case, 2 should be converted to 2/1.

'''