from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        x = s
        for i in range(len(spaces)):
            x = x[:spaces[i]+i]+' '+x[spaces[i]+i:]
        return x


#Exercise: https://leetcode.com/problems/adding-spaces-to-a-string/
#You are given a 0-indexed string s and a 0-indexed integer array spaces that describes
# the indices in the original string where spaces will be added. Each space should 
# be inserted before the character at the given index.