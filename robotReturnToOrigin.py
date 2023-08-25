class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = 0
        l = 0
        r = 0
        u = 0
        for x in moves: 
            if x == 'D':
                d += 1
            elif x == 'U': 
                u += 1
            elif x == 'L':
                l += 1
            elif x == 'R': 
                r += 1
        if u == d and l == r: 
            return True 
        return False
        
#https://leetcode.com/problems/robot-return-to-origin/
#There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given 
# a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
#You are given a string moves that represents the move sequence of the robot where moves[i] represents
#its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
#Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.