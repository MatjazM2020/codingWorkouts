class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        n, pos, neg = len(s), 0, 0
        for i in range(0, n, 2):
            pos += int(s[i])
        for i in range(1, n, 2):
            neg -= int(s[i])
        return pos+neg




'''
https://leetcode.com/problems/alternating-digit-sum/description/

You are given a positive integer n. Each digit of n has a sign
according to the following rules:

The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.
'''