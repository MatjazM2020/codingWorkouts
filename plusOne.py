from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in range(len(digits)): 
            s += str(digits.__getitem__(i))
        x = int(s)
        x += 1
        s = str(x)
        l = []
        for x in s: 
            l.append(int(x))
        return l


#Exercise: https://leetcode.com/problems/remove-element/
#Given an integer array nums and an integer val, remove all
# occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

