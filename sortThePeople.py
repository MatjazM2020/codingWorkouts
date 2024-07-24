from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        merged = [x for x in zip(names, heights)]
        merged = sorted(merged, reverse = True, key= lambda x: x[1])
        names = [x[0] for x in merged]
        return(names)

'''
https://leetcode.com/problems/sort-the-people/description/

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights

'''