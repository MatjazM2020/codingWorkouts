from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       nums = [i+1 for i in range(n)]
       return list(combinations(nums,k))
        
  
        
#https://leetcode.com/problems/combinations/description/
#Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

