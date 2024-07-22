from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pt1 = head
        pt2 = head.next

        while pt2:
            if pt2.val == 0: 
                if pt2.next is None:
                    pt1.next = None
                    break
                pt1.next = pt2
                pt1 = pt1.next
            pt1.val += pt2.val
            pt2 = pt2.next
        return head
    
    
'''
https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

You are given the head of a linked list, which contains a series of integers separated by 0's.
The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes.
The modified list should not contain any 0's.

Return the head of the modified linked list.
'''
