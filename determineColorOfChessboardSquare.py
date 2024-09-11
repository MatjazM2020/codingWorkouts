class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letters_odd = ['a', 'c', 'e', 'g']
        if coordinates[0] in letters_odd and int(coordinates[1])%2 == 0:
            return True
        if coordinates[0] not in letters_odd and int(coordinates[1])%2 == 1:
            return True
        return False
    
    
    
    
'''
https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/

You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

'''