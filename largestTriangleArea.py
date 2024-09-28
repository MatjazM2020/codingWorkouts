from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n, maxArea = len(points), 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x_1, y_1 = points[i]
                    x_2, y_2 = points[j]
                    x_3, y_3 = points[k]
                    area = 1/2*abs(x_1*(y_2-y_3) + x_2*(y_3-y_1) + x_3*(y_1-y_2))
                    maxArea = max(maxArea, area)
        return maxArea
    
    
    
'''
https://leetcode.com/problems/largest-triangle-area/description/

Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area
of the largest triangle that can be formed by any three different points. Answers within 10-5 
of the actual answer will be accepted.
'''