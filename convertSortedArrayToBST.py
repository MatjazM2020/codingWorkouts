class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums) == 0: 
            return None
        else: 
            return TreeNode(nums[len(nums)//2],self.sortedArrayToBST(nums[:len(nums)//2]),self.sortedArrayToBST(nums[(len(nums)//2)+1:]))
        
        
#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced
# binary search tree.

