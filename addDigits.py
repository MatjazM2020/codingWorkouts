class Solution:
    def addDigits(self, num: int) -> int:
        x = str(num)
        res = 0
        for c in x:
            res += int(c)
        if res//10 == 0:
            return res
        else: 
            return self.addDigits(res)

#Exercise: https://leetcode.com/problems/add-digits/
#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.