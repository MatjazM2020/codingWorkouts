from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, (m*n)-1
        while l <= r:
            c = l+(r-l)//2
            row = c//n
            col = c%n
            if matrix[row][col] < target:
                l = c+1
            elif matrix[row][col] > target:
                r = c-1
            else:
                return True
        return False


'''
https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=binary-search

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''