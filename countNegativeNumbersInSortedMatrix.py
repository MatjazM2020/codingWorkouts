from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                 if grid[i][j] < 0: 
                     count += 1
        return count
                
sol = Solution()
sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
#Given a m x n matrix grid which is sorted in non-increasing order both row-wise 
# and column-wise, return the number of negative numbers in grid.