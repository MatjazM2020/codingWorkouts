from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n, res, sm = len(grid), len(grid[0]), 0, 0
        for i in range(m-2):
            for j in range(n-2):
                sm = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                res = max(res, sm)
        return res
    
'''
https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

You are given an m x n integer matrix grid.

We define an hourglass as a part of the matrix with the following form:
[A B C]
[  D  ]
[E F G]

Return the maximum sum of the elements of an hourglass.

Note that an hourglass cannot be rotated and must be entirely contained within the matrix.



'''