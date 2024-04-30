

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def depth(self, root:Optional[TreeNode]) -> int: 
        if root == None: 
            return 0 
        if root.left == None and root.right == None: 
            return 1 
        if root.left != None and root.right != None:
            return 1 + max(self.depth(root.left), self.depth(root.right))
        if root.left != None: 
            return 1 + self.depth(root.left)
        if root.right != None: 
            return 1 + self.depth(root.right)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None: 
            return root.val
        if self.depth(root.left) > self.depth(root.right):
            return self.deepestLeavesSum(root.left)
        if self.depth(root.right) > self.depth(root.left): 
            return self.deepestLeavesSum(root.right)
        return self.deepestLeavesSum(root.left) + self.deepestLeavesSum(root.right)
    
    
    
# problem: https://leetcode.com/problems/deepest-leaves-sum/description/
# Given the root of a binary tree, return the sum of values of its deepest leaves.
 