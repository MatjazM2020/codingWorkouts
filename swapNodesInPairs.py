from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapHelper(self, head: Optional[ListNode],root: Optional[ListNode], prev:Optional[ListNode]): 
        if head == None:
            return root
        elif head.next == None: 
            return root
        else: 
            third = head.next.next
            temp = head
            head = head.next
            head.next = temp
            temp.next = third
            prev.next = head
            return self.swapHelper(third,root,head.next)
        
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None: 
            return head
        else: 
            third = head.next.next
            temp = head
            head = head.next
            head.next = temp
            temp.next = third
            return self.swapHelper(third,head,head.next)
    
        
#Exercise: https://leetcode.com/problems/swap-nodes-in-pairs/
#Given a linked list, swap every two adjacent nodes and return 
# its head. You must solve the problem without modifying the 
# values in the list's nodes (i.e., only nodes themselves may be changed.)
