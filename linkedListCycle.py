from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    flag = pow(10,5)+1
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        elif head.next == None:
            return False
        elif head.next.val == self.flag:
            return True
        else:
            head.val = self.flag
            return self.hasCycle(head.next)
           
            

#Excercise: https://leetcode.com/problems/linked-list-cycle/description/
#Given head, the head of a linked list, determine if the linked list has a cycle in it.
#There is a cycle in a linked list if there is some node in the list that can be reached
#again by continuously following the next pointer. Internally, pos is used to denote the 
#index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#Return true if there is a cycle in the linked list. Otherwise, return false.

