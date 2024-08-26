from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def checkRot(x: int) -> int:
            topEqual = 0
            botEqual = 0
            for i in range(len(tops)):
                if x != tops[i] and x != bottoms[i]:
                    return -1
                elif x != tops[i]:
                    topEqual += 1
                elif x != bottoms[i]:
                    botEqual += 1
            return min(topEqual, botEqual)
        
        return(max(checkRot(tops[0]), checkRot(bottoms[0])))
    
    
'''
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.
'''