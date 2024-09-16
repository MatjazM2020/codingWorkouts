from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutesPoints, n, minDiff, currDiff = [], len(timePoints), float('inf'), None
        for x in timePoints:
            y = x.split(':')
            minutesPoints.append(int(y[0])*60 + int(y[1]))
        minutesPoints.sort()
        for i in range(1, n):
            curDiff = minutesPoints[i]-minutesPoints[i-1]
            minDiff = min(curDiff, minDiff)
        minDiff = min((24*60)-(minutesPoints[-1]-minutesPoints[0]), minDiff)
        return minDiff
        
        
        
'''
https://leetcode.com/problems/minimum-time-difference/description/

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

'''