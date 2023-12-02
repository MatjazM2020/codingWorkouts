from ast import List
import copy
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dict = {}
        for x in chars: 
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        sm = 0
        for word in words:
            dictTemp = copy.deepcopy(dict)
            for i in range(len(word)): 
                if word[i] in dictTemp and dictTemp[word[i]] > 0:
                    dictTemp[word[i]] -= 1
                else: 
                    break
                if i == len(word)-1: 
                    sm += len(word)
        return sm
    
    
#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
#You are given an array of strings words and a string chars.
#A string is good if it can be formed by characters from chars (each character can only be used once).
#Return the sum of lengths of all good strings in words.