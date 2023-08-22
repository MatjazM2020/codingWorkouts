from typing import Optional

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
   def pathHelper(self, root:Optional[TreeNode], targetSum: int, travel:int): 
      if root == None: 
         return False
      else:
         travel += root.val
         if travel == targetSum and root.left == None and root.right == None:
            return True
         else:
            return self.pathHelper(root.left, targetSum, travel) or self.pathHelper(root.right, targetSum, travel)
         
         
   def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
         return self.pathHelper(root, targetSum, 0)



#https://leetcode.com/problems/path-sum/
#Given the root of a binary tree and an integer targetSum, return true if the tree has 
# a root-to-leaf path such that adding up all the values along the path equals targetSum.
#A leaf is a node with no children.