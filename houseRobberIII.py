from functools import cache
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def robber(root: Optional[TreeNode], parentRobbed: bool):
            if root == None: 
                return 0
            if not parentRobbed: 
                return max(root.val + robber(root.left, True) + robber(root.right, True), robber(root.left, False) + robber(root.right, False))
            else: 
                return (robber(root.left, False) + robber(root.right, False))
        return max(robber(root, False), robber(root, True))


#https://leetcode.com/problems/house-robber-iii/?envType=study-plan-v2&envId=dynamic-programming
#The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in
# this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.
# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.