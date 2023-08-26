class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def helperSum(self, root: Optional[TreeNode]) -> int: 
        if root == None:
            return 0
        return self.helperSum(root.left) + root.val + self.helperSum(root.right)
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return 0
        x = abs(self.helperSum(root.left)-self.helperSum(root.right))
        return x + self.findTilt(root.left) + self.findTilt(root.right)
        
        
      
#https://leetcode.com/problems/binary-tree-tilt/
#Given the root of a binary tree, return the sum of every tree node's tilt.
#The tilt of a tree node is the absolute difference between the sum of all left subtree node values
#and all right subtree node values. If a node does not have a left child, then the sum of the left
#subtree node values is treated as 0. The rule is similar if the node does not have a right child.