from typing import Optional

class ListNode:
    def __init__(self, val= 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeHelper(self, list1: Optional[ListNode], list2: Optional[ListNode], ls: Optional[ListNode], lsHead: Optional[ListNode]):
        if list1 == None:
            ls.next = list2
            return lsHead
        elif list2 == None:
            ls.next = list1 
            return lsHead
        if list1.val <= list2.val:
            ls.next = ListNode(list1.val)
            list1 = list1.next
            return self.mergeHelper(list1,list2,ls.next,lsHead)
        else:
            ls.next = ListNode(list2.val)
            list2 = list2.next
            return self.mergeHelper(list1,list2,ls.next,lsHead)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode])->Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        if list1.val <= list2.val:
            ls = ListNode(list1.val)
            list1 = list1.next
        else:
            ls = ListNode(list2.val)
            list2 = list2.next
        lsHead = ls
        return self.mergeHelper(list1, list2, ls, lsHead)
        

#just testing below ........
inst = Solution()
ls1 = ListNode(2,ListNode(3))
ls2 = ListNode(1,ListNode(5))

x = inst.mergeTwoLists(ls1,ls2)

for i in range(4):
    print(x.val)
    x = x.next
#.......................
#excercise: https://leetcode.com/problems/merge-two-sorted-lists/
#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists into one sorted list. The list should be made by
#splicing together the nodes of the first two lists.
#Return the head of the merged linked list.
