class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def insert(root, val):
            if root == None:
                return TreeNode(val)
            if root.val < val:
                root.right = insert(root.right, val)
            elif root.val > val:
                root.left = insert(root.left, val)
            return root
        root = None
        for val in preorder:
            root = insert(root, val)
        return root
    
    
'''
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), 
construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the
given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than
Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then
traverses Node.right.



'''