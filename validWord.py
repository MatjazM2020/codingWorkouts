import string


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        letters, numbers = set(string.ascii_letters), set(str(x) for x in range(10))
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        allChars, vowIs, consIs = letters.union(numbers), False, False
        for x in word:
            if x not in allChars: return False
            if x in vowels: vowIs = True
            if x in letters and (x not in vowels): consIs = True
        return vowIs and consIs


'''
https://leetcode.com/problems/valid-word/

A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.

'''