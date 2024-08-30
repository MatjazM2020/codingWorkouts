from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        def checkEquation(xj, yj, rj, xi, yi):
            return (xi - xj)**2 + (yi-yj)**2 <= rj**2 
        
        arr = []
        for xj, yj, rj in queries:
            arr.append(0)
            for xi, yi in points:
                if checkEquation(xj, yj, rj, xi, yi):
                    arr[-1] += 1
        return arr
    
    

'''
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/description/

You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane.
Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.

'''