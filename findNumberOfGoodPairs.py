from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m, count = len(nums1), len(nums2), 0

        for i in range(n):
            for j in range(m):
                if nums1[i]%(nums2[j]*k) == 0:
                    count += 1
        return count
    
    
    
'''
https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/

You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.

'''