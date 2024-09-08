from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        hd, length = head, 0
        while hd:
            length += 1
            hd = hd.next

        splitLen = length//k
        numAdded = length%k

        hd, res, count, tempList = head, [], 1, head
        for _ in range(k):
            curr = hd
            currLen = splitLen + (1 if numAdded > 0 else 0)
            numAdded -= 1

            for _ in range(currLen-1):
                if hd:
                    hd = hd.next
            if hd:
                nextPart = hd.next
                hd.next = None
                hd = nextPart
            res.append(curr)

        return res
    
    
'''
https://leetcode.com/problems/split-linked-list-in-parts/description/?envType=daily-question&envId=2024-09-08

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. 
This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a
size greater than or equal to parts occurring later.

Return an array of the k parts.
'''