from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    dict = {}
    def palindromeHelper(self,head:Optional[ListNode], i: int) -> int: 
       if head != None:
            self.dict[i] = head.val
            return self.palindromeHelper(head.next,i+1)
       else: 
            return i
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = self.palindromeHelper(head,0)
        rs = (x//2)
        for i in range(rs): 
            if self.dict[i] != self.dict[x-1-i]: 
                return False
        return True



#Exercise: https://leetcode.com/problems/palindrome-linked-list/
#Given the head of a singly linked list, return true if it is a palindrome
# or false otherwise.