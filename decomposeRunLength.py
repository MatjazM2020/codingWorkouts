from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        i = 0

        while (i*2)+1 < n:
            res += [nums[(i*2)+1]]*nums[i*2]
            i += 1
        return res

    
    
'''
https://leetcode.com/problems/decompress-run-length-encoded-list/description/

We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair,
there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
'''