from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
        
        current = head
        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head
        



'''
https://leetcode.com/problems/remove-linked-list-elements/description/


Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

'''