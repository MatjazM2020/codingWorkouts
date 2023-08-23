class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for x in magazine: 
            try: 
                dict[x] += 1
            except:
                dict[x] = 1
        for x in ransomNote:
            try:
                dict[x] -= 1
                if dict[x] < 0:
                    return False
            except:
                return False
        return True


#https://leetcode.com/problems/ransom-note/
#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by
# using the letters from magazine and false otherwise. Each letter in magazine can only be used once in ransomNote.
