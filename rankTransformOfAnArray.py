from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(set(arr))
        dic = {val: rank + 1 for rank, val in enumerate(sortedArr)}
        return [dic[x] for x in arr]
    
    
    
    
'''
https://leetcode.com/problems/rank-transform-of-an-array/

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
'''
