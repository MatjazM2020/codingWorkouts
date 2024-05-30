from functools import cache
from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)-1
        @cache
        def helper(i: int) -> int:
            if i > n:
                return 0 
            return max(questions[i][0]+helper(questions[i][1]+i+1), helper(i+1))
        return helper(0)


'''
https://leetcode.com/problems/solving-questions-with-brainpower/description/?envType=study-plan-v2&envId=dynamic-programming
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0)
and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable
to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.
'''


