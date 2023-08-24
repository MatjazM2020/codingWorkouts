from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def helper(self, root: Optional[TreeNode], i: int)-> int: 
        if root.left == None and root.right != None: 
            return self.helper(root.right, i+1)
        elif root.left != None and root.right == None: 
            return self.helper(root.left, i+1)
        elif root.left == None and root.right == None:
            return i
        else: 
            return min(self.helper(root.left, i+1), self.helper(root.right,i+1))
        
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return 0
        else: 
            return self.helper(root,1)




#https://leetcode.com/problems/minimum-depth-of-binary-tree/
#Given a binary tree, find its minimum depth.
#The minimum depth is the number of nodes along the shortest path 
# from the root node down to the nearest leaf node.