import random
from typing import List
class Solution:
    def __init__(self, w: List[int]):
        self.x = []
        self.totSum = sum(w)
        self.size = len(w)-1
        cum = 0
        for weight in w:
            cum += weight
            self.x.append(cum)
    def pickIndex(self) -> int:
        rand = random.uniform(0,self.totSum)
        l, r = 0, self.size
        while l < r:
            c = l + (r - l)//2
            if self.x[c] < rand:
                l = c + 1
            else:
                r = c
        return l
    
    
    
'''
https://leetcode.com/problems/random-pick-with-weight/description/?envType=study-plan-v2&envId=binary-search

You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] 
(inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability
of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

'''