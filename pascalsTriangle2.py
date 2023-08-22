from typing import List

class Solution:
   def getRow(self, rowIndex: int) -> List[int]:
      rowIndex += 1
      x = [[1],[1,1]]
      if rowIndex == 1: 
         return [1]
      elif rowIndex == 2: 
         return [1,1]
      else:
       for i in range(2,rowIndex):
         y = []
         for j in range(0,i+1): 
            if j == 0 or j == i: 
               y.append(1)
            else: 
               y.append(x[i-1][j-1]+x[i-1][j])
         x.append(y)
      return x[rowIndex-1]    

       
#Given an integer numRows, return the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

