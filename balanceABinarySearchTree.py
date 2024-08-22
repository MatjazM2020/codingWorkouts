
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        tr = None
        def inorderTraversal(r):
            if r is None:
                return []
            return inorderTraversal(r.left) + [r.val] + inorderTraversal(r.right)
        arr = inorderTraversal(root)
        
        def insert(arr):
            if not arr:
                return None
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = insert(arr[:mid])
            root.right = insert(arr[mid+1:])
            return root

        return insert(arr)
    

'''
https://leetcode.com/problems/balance-a-binary-search-tree/description/

Given the root of a binary search tree, return a balanced binary search tree with the same node values. 
If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
'''