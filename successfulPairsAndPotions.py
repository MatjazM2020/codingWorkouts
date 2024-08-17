from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)-1
        res = []
        potions.sort()
        for spell in spells:
            l, r = 0, n
            while l <= r:
                c = l + (r - l)//2
                if potions[c]*spell >= success:
                    r = c - 1
                else:
                    l = c + 1
            res.append(n-r)
        return res
    
    
'''
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=binary-search

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the
strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
'''