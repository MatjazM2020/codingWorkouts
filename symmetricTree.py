from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p == None and q == None: 
                return True
            elif (p == None and q != None) or (p != None and q == None):
                return False
            elif p.val == q.val: 
                return self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left)
            else: 
                return False
            
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None: 
            return True
        elif (root.left == None and root.right != None) or (root.left != None and root.right == None):
            return False
        else: 
            return self.isSameTree(root.left, root.right)
 
 

 
#Exercise: https://leetcode.com/problems/symmetric-tree/
#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
