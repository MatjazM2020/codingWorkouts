from typing import List

class Solution:
   def generate(self, numRows: int) -> List[List[int]]:
      x = [[1],[1,1]]
      if numRows == 1: 
         return [[1]]
      elif numRows == 2: 
         return [[1],[1,1]]
      else:
       for i in range(2,numRows):
         y = []
         for j in range(0,i+1): 
            if j == 0 or j == i: 
               y.append(1)
            else: 
               y.append(x[i-1][j-1]+x[i-1][j])
         x.append(y)
      return x       

       
#Given an integer numRows, return the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

