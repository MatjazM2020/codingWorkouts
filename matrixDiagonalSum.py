from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        for i in range(n):
            sum += mat[i][i] + mat[i][n-i-1]
        if n%2 == 1: 
            return sum - mat[(n)//2][(n)//2]
        return sum
        
    
#https://leetcode.com/problems/matrix-diagonal-sum/
#Given a square matrix mat, return the sum of the matrix diagonals.
#Only include the sum of all the elements on the primary diagonal and all the 
# elements on the secondary diagonal that are not part of the primary diagonal.

