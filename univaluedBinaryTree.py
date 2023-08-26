from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root.left != None and root.right == None:
            if root.val != root.left.val:
                return False
            else: 
                return self.isUnivalTree(root.left)
        elif root.left == None and root.right != None: 
            if root.val != root.right.val:
                return False
            else: 
                return self.isUnivalTree(root.right)
        elif root.left == None and root.right == None: 
                return True
        elif root.val != root.left.val or root.val != root.right.val:
             return False
        else: 
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
         

#https://leetcode.com/problems/univalued-binary-tree/
#A binary tree is uni-valued if every node in the tree has the same value.
#Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.