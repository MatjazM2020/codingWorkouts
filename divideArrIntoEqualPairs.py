from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}
        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        for x in freq:
            if freq[x]%2 != 0:
                return False
        return True



'''
https://leetcode.com/problems/divide-array-into-equal-pairs/description/

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

'''