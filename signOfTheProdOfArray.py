from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for x in nums: 
            if x < 0: 
                res *= -1
            elif x == 0: 
                return 0 
        return res

'''
https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
'''