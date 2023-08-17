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
           
            


