from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteHelper(self, head: Optional[ListNode], root: Optional[ListNode]) -> Optional[ListNode]: 
        if head.next == None: 
            return root
        elif head.next.next == None: 
            if head.val == head.next.val: 
                head.next = None
                return root
            else: 
                return root
        else: 
            if head.val == head.next.val:
                head.next = head.next.next 
                return self.deleteHelper(head,root)
            else:
                return self.deleteHelper(head.next,root)
                
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head
        return self.deleteHelper(head,head)
        
        
#Excercise: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#Given the head of a sorted linked list, delete all duplicates such that each element
# appears only once. Return the linked list sorted as well.