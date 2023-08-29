from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def helper(self, root: Optional[TreeNode]) -> List[int]: 
        if root == None: 
            return []
        else:
            return [root.val] + self.helper(root.left) + self.helper(root.right)
           
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        a = self.helper(root)
        min = 999999
        for i in range(len(a)): 
            for j in range(i+1,len(a)): 
                if abs(a[i] - a[j]) < min: 
                    min = abs(a[i] - a[j]) 
        return min
        
#https://leetcode.com/problems/minimum-distance-between-bst-nodes/
#Given the root of a Binary Search Tree (BST), return the minimum difference
# between the values of any two different nodes in the tree.