from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        pt1 = 0
        pt2 = n-1
        mx = 0
        while pt1 < pt2: 
            vol = (pt2 - pt1)*(min(height[pt1], height[pt2]))
            if vol > mx:
                mx = vol
            if height[pt1] > height[pt2]:
                pt2 -= 1
            else:
                pt1 += 1
        return(mx)
    


'''
https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''