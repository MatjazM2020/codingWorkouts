from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    dict = {}
    def middleHelper(self, head: Optional[ListNode], i: int) -> int:
        if head != None: 
         self.dict[i] = head
         return self.middleHelper(head.next,i+1)
        else:
            return i
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        elif head.next.next == None:
            return head.next
        a = self.middleHelper(head, 0)
        if len(self.dict)%2 == 0:
                return self.dict[(a//2)]
        else:
                return self.dict[a//2]
            



#Exercise: https://leetcode.com/problems/middle-of-the-linked-list/
#Given the head of a singly linked list, return the middle node of the linked list.
#If there are two middle nodes, return the second middle node.