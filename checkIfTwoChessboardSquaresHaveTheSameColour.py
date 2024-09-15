class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def squareIsWhite(coordinates):
            letters_odd = ['a', 'c', 'e', 'g']
            if coordinates[0] in letters_odd and int(coordinates[1])%2 == 0:
                return True
            if coordinates[0] not in letters_odd and int(coordinates[1])%2 == 1:
                return True
            return False
        if squareIsWhite(coordinate1) == squareIsWhite(coordinate2):
            return True
        return False

        
'''
https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/

You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square 
on an 8 x 8 chessboard.
Below is the chessboard for reference.

Return true if these two squares have the same color and false otherwise.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter
first (indicating its column), and the number second (indicating its row).

'''