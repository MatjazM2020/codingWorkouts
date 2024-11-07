from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = [0]
        def height(node):
            if node:
                height_left = height(node.left)
                height_right = height(node.right)
                diam[0] = max(diam[0], height_left + height_right)
                return 1 + max(height_left, height_right)
            else:
                return 0
        height(root)
        return diam[0]
    
    
    
'''
https://leetcode.com/problems/diameter-of-binary-tree/description/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

'''