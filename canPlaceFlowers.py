from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                res += 1
                
        for i in range(1,len(flowerbed)-1): 
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                res += 1
        if flowerbed[len(flowerbed)-2] == 0 and flowerbed[len(flowerbed)-1] == 0:
            res += 1
        if n <= res:
            return True   
        else: 
            return False
                
        
        
        
#https://leetcode.com/problems/can-place-flowers/
#You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot
# be planted in adjacent plots.
#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an 
# integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers
# rule and false otherwise.