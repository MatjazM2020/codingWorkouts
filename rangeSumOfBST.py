from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int: 
       if root == None: 
          return 0
       elif root.val <= high and root.val >= low: 
          return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
       else:
          return self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)
         
       
#https://leetcode.com/problems/range-sum-of-bst/
#Given the root node of a binary search tree and two integers low and high, 
# return the sum of values of all nodes with a value in the inclusive range [low, high].