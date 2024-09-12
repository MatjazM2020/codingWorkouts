class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        alphabet = {
            'a':(0,0),'b':(0,1),'c':(0,2),'d':(0,3),'e':(0,4)
            ,'f':(1,0),'g':(1,1),'h':(1,2),'i':(1,3),'j':(1,4)
            ,'k':(2,0),'l':(2,1),'m':(2,2),'n':(2,3),'o':(2,4)
            ,'p':(3,0),'q':(3,1),'r':(3,2),'s':(3,3),'t':(3,4)
            ,'u':(4,0),'v':(4,1),'w':(4,2),'x':(4,3),'y':(4,4)
            ,'z':(5,0)
        }

        start, res, specCase = (0,0), '', False
        for x in target:
            if start == alphabet[x]:
                res += '!'
                continue
            if x == 'z':
                specCase = True
                x = 'u'
            end = alphabet[x]
            ver = end[0]-start[0]
            hor = end[1]-start[1]
            if ver < 0:
                res += 'U'*(-ver)
            elif ver > 0:
                res += 'D'*ver
            if hor < 0:
                res += 'L'*(-hor)
            elif hor > 0:
                res += 'R'*(hor)
            if specCase:
                res += 'D'
                x = 'z'
                specCase = False
            res += '!'
            start = alphabet[x]
        return res




'''
https://leetcode.com/problems/alphabet-board-path/description/

On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves. 
You may return any path that does so.
'''