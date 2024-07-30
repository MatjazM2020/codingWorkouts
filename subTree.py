class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r, s):
            if not r and not s:
                return True
            elif not r or not s:
                return False
            if r.val == s.val: 
                return(isSame(r.left, s.left) and isSame(r.right, s.right))
        def check(r, s):
            if not r:
                return False
            else:
                return isSame(r, s) or check(r.left, s) or check(r.right, s)
        return check(root, subRoot)
    


'''
https://leetcode.com/problems/subtree-of-another-tree/description/

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same 
structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.
'''
