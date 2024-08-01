class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        intervals = [intervals[i] + [i] for i in range(n)]
        srt = sorted(intervals, key = lambda x: x[0])
        res = [0]*n
        def findRight(x):
            l = 0
            r = n-1
            c = 0
            capture = 0
            while l <= r:
                c = (l+r)//2 
                if srt[c][0] > x[1]:
                    capture = srt[c][2]
                    r = c - 1
                elif srt[c][0] < x[1]:
                    if c >= n-1:
                        return -1
                    l = c + 1
                else:
                    capture = srt[c][2]
                    break
            return(capture)
        for i in range(n):
            res[srt[i][2]] = findRight(srt[i])
        return res



'''
https://leetcode.com/problems/find-right-interval/?envType=study-plan-v2&envId=binary-search
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.
'''