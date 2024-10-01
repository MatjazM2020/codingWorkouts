from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        remCount = [0]*k
        for x in arr:
            rem = x%k
            remCount[rem] += 1
        for i in range(1,(k//2)+1):
            if remCount[i] != remCount[k-i]: return False
        if remCount[0]%2 != 0: return False
        if k%2 == 0 and remCount[(k//2)]%2 != 0: return False
        return True
    
    
    
'''
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.
'''