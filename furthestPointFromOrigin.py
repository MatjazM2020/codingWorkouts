class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        under = 0
        left = 0
        right = 0
        for a in moves: 
            if a == 'L': 
                left += 1
            elif a == 'R': 
                right += 1
            else: 
                under += 1
        if right > left: 
            return (right+under)-left
        else: 
            return (left+under)-right


#https://leetcode.com/problems/furthest-point-from-origin/
#You are given a string moves of length n consisting only of characters 'L', 'R', 
# and '_'. The string represents your movement on a number line starting from the origin 0.
#In the ith move, you can choose one of the following directions:
#move to the left if moves[i] = 'L' or moves[i] = '_'
#move to the right if moves[i] = 'R' or moves[i] = '_'
#Return the distance from the origin of the furthest point you can get to after n moves.