from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sumHelper(self, root: Optional[TreeNode]) -> int: 
        if root.left == None and root.right == None: 
            return root.val
        elif root.left != None and root.right != None: 
            if root.right.left != None or root.right.right != None: 
                return (self.sumHelper(root.left) + self.sumHelper(root.right))
            else: 
                return self.sumHelper(root.left)
        elif root.left != None and root.right == None: 
            return self.sumHelper(root.left)
        elif root.left == None and root.right != None: 
            if root.right.left != None or root.right.right != None: 
                return self.sumHelper(root.right)
            else:
                return 0
            
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None: 
           return 0
        return self.sumHelper(root)
            
#https://leetcode.com/problems/sum-of-left-leaves/
#Given the root of a binary tree, return the sum of all left leaves.
#A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.