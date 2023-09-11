from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1,m): 
            for j in range(1,n): 
                if matrix[i][j] == '1': 
                    matrix[i][j] = str(min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])) + 1)
        max = 0
        for i in range(m):
            for j in range(n): 
               if int(matrix[i][j]) > max: 
                   max = int(matrix[i][j])
        return max*max


#https://leetcode.com/problems/maximal-square/description/?envType=study-plan-v2&envId=dynamic-programming
#Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.