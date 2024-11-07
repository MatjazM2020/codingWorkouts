class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_p = abbr_p = 0

        while word_p < len(word) and abbr_p < len(abbr):
            if abbr[abbr_p].isdigit():
                steps = 0
                if abbr[abbr_p] == '0':
                    return False
                while abbr_p < len(abbr) and abbr[abbr_p].isdigit():
                    steps = steps*10 + int(abbr[abbr_p])
                    abbr_p += 1
                word_p += steps
            else:
                if word[word_p] != abbr[abbr_p]:
                    return False
                word_p += 1
                abbr_p += 1
        if word_p == len(word) and abbr_p == len(abbr):
            return True
        return False
    
    
    
'''
https://leetcode.com/problems/valid-word-abbreviation/

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.


'''