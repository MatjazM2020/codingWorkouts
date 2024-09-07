from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        def checker(hd, rt):
            if not hd:
                return True
            if not rt:
                return False
            if hd.val == rt.val:
                return checker(hd.next, rt.left) or checker(hd.next, rt.right)
            return False
        return checker(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    
'''
https://leetcode.com/problems/linked-list-in-binary-tree/description/

Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

'''