from typing import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        set1, d, res = set(), Counter(s), 0
        for x in s:
            set1.add(x)
            d[x] = max(d[x]-1, 0)
            if d[x] == 0: del d[x]
            if len(set1) == len(d):
                res += 1
        return res
    
    
'''
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/

You are given a string s.

A split is called good if you can split s into two non-empty strings sleft and sright where
their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct 
letters in sleft and sright is the same.

Return the number of good splits you can make in s.

'''