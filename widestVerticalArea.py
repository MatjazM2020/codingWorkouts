class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        points = sorted(points, key=lambda x: x[0])
        mx = -1
        for i in range(1,n):
            subt = points[i][0] - points[i-1][0]
            if subt > mx:
                mx = subt
        return(mx)




'''
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/

Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

'''