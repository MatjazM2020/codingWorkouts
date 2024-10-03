
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        r, refB, c = list1, None, 1
        while r:
            if c == b+2:
                refB = r
            r = r.next
            c += 1
        r = list1
        r2, c = list2, 1
        while r2:
            if not r2.next:
                r2.next = refB
                break
            r2 = r2.next
        while r.next:
            if c == a: 
                r.next = list2
                break
            r = r.next
            c += 1
        return list1
    

'''
https://leetcode.com/problems/merge-in-between-linked-lists/description/
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:

Build the result list and return its head.

'''