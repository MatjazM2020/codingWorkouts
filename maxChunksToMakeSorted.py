class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        i, k, curr, res = 0, 0, [], 0
        while k < len(arr):
            if curr + sorted(arr[i:k]) == list(range(k)):
                res += 1
                curr += sorted(arr[i:k])
                i = k
            k += 1
        return res
    
    
    
    
    
    
'''
https://leetcode.com/problems/max-chunks-to-make-sorted/description/?envType=daily-question&envId=2024-12-19

You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating 
them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

'''
