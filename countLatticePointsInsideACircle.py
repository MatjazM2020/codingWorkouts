import math
from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for x,y,r in circles:
            for i in range(math.floor(x - r), math.ceil(x + r)+1):
                for j in range(math.floor(y - r), math.ceil(y + r)+1):
                    if (i-x)**2 + (j-y)**2 <= r**2:
                        points.add((i,j))
        return len(points)
    
    
    
'''
https://leetcode.com/problems/count-lattice-points-inside-a-circle/description/

Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and
radius ri of the ith circle drawn on a grid, return the number of lattice points that are present
inside at least one circle.

Note:

A lattice point is a point with integer coordinates.
Points that lie on the circumference of a circle are also considered to be inside it.

'''