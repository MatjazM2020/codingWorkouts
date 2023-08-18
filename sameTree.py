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
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else: 
                return False
 
#https://leetcode.com/problems/same-tree/            
#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

