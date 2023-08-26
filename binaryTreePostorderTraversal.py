from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: 
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
      
      
#https://leetcode.com/problems/binary-tree-postorder-traversal/
#Given the root of a binary tree, return the postorder traversal of its nodes' values.