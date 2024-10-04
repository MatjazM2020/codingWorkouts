from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_sum, double_digit_sum = 0, 0
        for num in nums:
            if num < 10: single_digit_sum += num
            else: double_digit_sum += num
        return single_digit_sum != double_digit_sum
    
'''
https://leetcode.com/problems/find-if-digit-game-can-be-won/description/

You are given an array of positive integers nums.

Alice and Bob are playing a game. In the game, Alice can choose either all single-digit
numbers or all double-digit numbers from nums, and the rest of the numbers are given to
Bob. Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.

Return true if Alice can win this game, otherwise, return false.
'''