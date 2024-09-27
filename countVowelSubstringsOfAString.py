class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels, res, n = {'a', 'e', 'i', 'o', 'u'}, 0, len(word)
        for i in range(n-4):
            j = 5
            while i+j <= n:
                if set(word[i:i+j]) == vowels: res += 1
                j += 1
        return res
    
    
'''
https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

A substring is a contiguous (non-empty) sequence of characters within a string.
A vowel substring is a substring that only consists of vowels
('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
Given a string word, return the number of vowel substrings in word.
'''