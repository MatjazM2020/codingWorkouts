from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        removes, hd = set(nums), head
        
        while hd.next != None:
            if hd.next.val in removes:
                hd.next = hd.next.next
            else:
                hd = hd.next
        
        if head is not None and head.val in removes:
            head = head.next
        return head
    
    

'''
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2024-09-06

You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all
nodes from the linked list that have a value that exists in nums.

'''