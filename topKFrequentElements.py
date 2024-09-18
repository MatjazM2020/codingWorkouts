from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x, res = Counter(nums).most_common(k), []
        for val, occ in x:
            res += [val]
        return res
    
    
'''
https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

'''