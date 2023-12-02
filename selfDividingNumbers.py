class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ls = []
        for x in range(left,right+1): 
            a = str(x)
            for i in range(len(a)): 
                if int(a[i]) == 0 or x%int(a[i]) != 0: 
                    break 
                elif i == len(a)-1:
                    ls.append(x)
        return ls


# https://leetcode.com/problems/self-dividing-numbers/
#A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

