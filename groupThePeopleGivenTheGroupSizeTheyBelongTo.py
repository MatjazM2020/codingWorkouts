from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d, res = {}, []
        for i in range(len(groupSizes)):
            if groupSizes[i] in d:
                d[groupSizes[i]].append(i)
            else:
                d[groupSizes[i]] = [i]
        for x in d:
            s = len(d[x])
            bucket = []
            for i in range(s):
                bucket.append(d[x][i])
                if len(bucket) == x:
                    res.append(bucket)
                    bucket = []
        return res
            
            
'''
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/

There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example,
if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return
any of them. It is guaranteed that there will be at least one valid solution for the given input.

'''