class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if not(s[i] in s[i+1:]) and not(s[i] in s[:i]):
                return i
        return -1

#https://leetcode.com/problems/first-unique-character-in-a-string/
#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.