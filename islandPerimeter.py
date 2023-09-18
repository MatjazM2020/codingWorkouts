from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per = 0
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
             if grid[i][j] == 1:
                if i == 0: 
                    per += 1
                if i == len(grid)-1:
                    per += 1
                if j == 0: 
                        per += 1
                if j == len(grid[0])-1: 
                        per += 1
                if i > 0: 
                    if grid[i-1][j] == 0: 
                        per += 1
                if i < len(grid)-1: 
                    if grid[i+1][j] == 0: 
                        per += 1
                if j > 0: 
                    if grid[i][j-1] == 0: 
                        per += 1
                if j < len(grid[0])-1: 
                    if grid[i][j+1] == 0: 
                        per += 1
        return per
        
        
#You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there 
# is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes", meaning the water inside
# isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and
# height don't exceed 100. Determine the perimeter of the island.