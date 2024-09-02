from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = [sum(grid[i]) for i in range(m)]
        cols = [sum(row[i] for row in grid) for i in range(len(grid[0]))]
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = 2*(rows[i] + cols[j]) - m - n
        return res
    
    
'''
https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/

You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.



'''