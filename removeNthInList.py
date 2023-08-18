from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    node_dict = {}
    def removeHelper(self, head:Optional[ListNode], n:int, i: int) -> int: 
        if head == None: 
            return i-1
        self.node_dict[i] = head
        return self.removeHelper(head.next,n,i+1)
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        if head.next == None:
            return None
        size = self.removeHelper(head,n,1)
        indx = size+1-n
        if indx < size:
         (self.node_dict[indx-1]).next = self.node_dict[indx+1]
        else:
            self.node_dict[indx-1].next = None
        return head






#idea: we traverse the thing and keep track of the indices, and save the thing into a dictionary 
# at the end, we get the last index (the length, subtract the n, and reconnect the things accordingly)
# then we return the head of this new modified list 


#Exercise: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#Given the head of a linked list, remove the nth node from the end of the list and return its head.