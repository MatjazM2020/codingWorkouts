from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = [((0,0),(2,2)),
        ((0,3),(2,5)),
        ((0,6),(2,8)),
        ((3,0),(5,2)),
        ((3,3),(5,5)),
        ((3,6),(5,8)),
        ((6,0),(8,2)),
        ((6,3),(8,5)),
        ((6,6),(8,8))]

        for i in range(9):
            l.append(((i,0),(i,8)))
            l.append(((0,i),(8,i)))

        def checkArea(coord1, coord2):
            x1, y1 = coord1
            x2, y2 = coord2
            seen = set()
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if board[i][j] != '.' and board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True
        
        for x in l:
            coord1, coord2 = x
            if not checkArea(coord1, coord2):
                return False
        return True
    
    
'''
https://leetcode.com/problems/valid-sudoku/description/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''