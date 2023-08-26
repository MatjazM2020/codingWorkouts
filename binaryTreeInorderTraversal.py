from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if root == None:
         return []
      return self.inorderTraversal(root.left)+ [root.val] + self.inorderTraversal(root.right)
      
      
      
#https://leetcode.com/problems/binary-tree-inorder-traversal/
#Given the root of a binary tree, return the inorder traversal of its nodes' values.