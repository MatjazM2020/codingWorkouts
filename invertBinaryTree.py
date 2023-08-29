from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertHelper(self, root: Optional[TreeNode], origin: Optional[TreeNode]) -> None:
        if root == None:
            pass
        else:
            temp = root.right
            root.right = root.left 
            root.left = temp
            self.invertHelper(root.left, origin)
            self.invertHelper(root.right, origin)
            
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertHelper(root, root)
        return root
        




#https://leetcode.com/problems/invert-binary-tree/
#Given the root of a binary tree, invert the tree, and return its root.