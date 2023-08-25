from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        a = []
        for i in range(n+1): 
            x = str(bin(i)[2:])
            c = 0
            for i in x: 
                if i == '1':
                    c += 1
            a.append(c)
        return a


#https://leetcode.com/problems/counting-bits/
#Given an integer n, return an array ans of length n + 1 such that for each
# i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

