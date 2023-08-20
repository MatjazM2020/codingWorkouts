from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depthHelper(self, root:Optional[TreeNode], depth: int) -> int: 
        if root.left != None and root.right != None: 
            return max(self.depthHelper(root.left, depth+1), self.depthHelper(root.right,depth+1))
        elif root.left != None: 
            return self.depthHelper(root.left,depth+1)
        elif root.right != None: 
            return self.depthHelper(root.right,depth+1)
        else:
            return depth
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.depthHelper(root,1)


#Exercise: https://leetcode.com/problems/maximum-depth-of-binary-tree/
#Given the root of a binary tree, return its maximum depth.
#A binary tree's maximum depth is the number of nodes along the
#longest path from the root node down to the farthest leaf node.