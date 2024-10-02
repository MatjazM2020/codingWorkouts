
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.cum = 0
        def helper(rt):
            if not rt: return None
            helper(rt.right)
            self.cum += rt.val
            rt.val = self.cum
            helper(rt.left)
        helper(root)
        return root
    
    
'''
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the 
original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''