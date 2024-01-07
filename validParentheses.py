class Solution(object):
    def isValid(self, s):
        x = []
        for a in s: 
            if a in {'(','[','{'}:
                 x.append(a)
            elif a == ')' and x and x[-1] == '(':
                x.pop()
            elif a == ']' and x and x[-1] == '[':
                x.pop()
            elif a == '}' and x and x[-1] == '{':
                x.pop()
            else: 
                return False
        if x:
            return False
        return True



#https://leetcode.com/problems/valid-parentheses/
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.