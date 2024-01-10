class Solution(object):
    def reverseWord(self, s): 
        a = ''
        for x in s: 
            a = x + a 
        return a
    def reverseWords(self, s):
        result = ''
        ls = split(s)
        for elt in ls: 
            result += self.reverseWord(elt) + ' '
        return result.rstrip()
    
    
    
    
#https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#Given a string s, reverse the order of characters in each word 
#within a sentence while still preserving whitespace and initial word order.
    