from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        x = [(i, score[i][k]) for i in range(len(score))]
        x.sort(key=lambda a: a[1], reverse=True)
        res = []
        for a in x:
            res.append(score[a[0]])
        return res
    
    
    
'''
https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/
There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, where each
row represents one student and score[i][j] denotes the score the ith student got in the jth exam. The matrix score
contains distinct integers only.

You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in the kth
(0-indexed) exam from the highest to the lowest.

Return the matrix after sorting it.
'''