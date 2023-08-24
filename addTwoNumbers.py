from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def helperAdd(self, l: Optional[ListNode], s:str, i: int, r: Optional[ListNode]) -> Optional[ListNode]:
        if i == -1:
            return r
        else: 
            l.next = ListNode(s[i])
            return self.helperAdd(l.next, s, i-1, r)
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ''
        while l1 != None: 
            str1 += str(l1.val)
            l1 = l1.next
        str2 = ''
        while l2 != None: 
            str2 += str(l2.val)
            l2 = l2.next
        str11 = ''
        for i in range(len(str1)-1,-1,-1):
            str11 += str1[i]
        int1 = int(str11)
        str22 = ''
        for i in range(len(str2)-1,-1,-1):
            str22 += str2[i]
        int2 = int(str22)
        r = int1+int2
        s = str(r)
        l = ListNode(s[len(s)-1])
        return self.helperAdd(l,s,len(s)-2,l)
                
        
l1 = ListNode(2, ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6, ListNode(4)))
sol = Solution()
print(sol.addTwoNumbers(l1,l2))



#https://leetcode.com/problems/add-two-numbers/
#You are given two non-empty linked lists representing two non-negative integers. The digits 
# are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers
# and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.