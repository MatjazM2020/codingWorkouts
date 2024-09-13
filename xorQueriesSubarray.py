from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixSums, prefix = [], 0
        for i in range(len(arr)):
            prefix ^= arr[i]
            prefixSums.append(prefix)
        res = []
        for query in queries:
            left, right = query[0], query[1]
            res.append(prefixSums[left] ^ prefixSums[right] ^ arr[left])
        return res
    
    
    
'''
https://leetcode.com/problems/xor-queries-of-a-subarray/description/

You are given an array arr of positive integers. You are also given the array queries
where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR
arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.

'''