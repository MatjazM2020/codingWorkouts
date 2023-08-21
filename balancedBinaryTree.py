from typing import Optional

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


class Solution:
   def height(self,root:Optional[TreeNode], depth:int)-> int:
      if root == None:
         return depth
      elif root.left != None and root.right != None: 
         return max(self.height(root.left, depth+1),self.height(root.right,depth+1))
      elif root.left == None and root.right != None: 
         return self.height(root.right,depth+1)
      elif root.left != None and root.right == None: 
         return self.height(root.left,depth+1)
      else: 
         return depth+1
      
   def isBalanced(self, root: Optional[TreeNode]) -> bool:
      if root == None: 
         return True
      elif abs(self.height(root.left,0)-self.height(root.right,0)) > 1:
         return False
      else: 
         return self.isBalanced(root.left) and self.isBalanced(root.right)
         
          
x = TreeNode(0,None,TreeNode(1,None,TreeNode(2,None,None)))
sol = Solution()
print(sol.isBalanced(x))


#https://leetcode.com/problems/balanced-binary-tree/
#Given a binary tree, determine if it is height-balanced