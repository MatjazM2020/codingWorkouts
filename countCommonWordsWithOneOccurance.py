from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict1 = {}
        for x in words1:
            if x not in dict1:
                dict1[x] = 1
            else:
                dict1[x] += 1
        dict2 = {}
        for y in words2:
            if y not in dict2:
                dict2[y] = 1
            else:
                dict2[y] += 1
        
        intersect = set(words1).intersection(set(words2))

        count = 0
        for x in intersect:
            if dict1[x] == 1 and dict2[x] == 1:
                count += 1
        return count
    
    
    '''
    https://leetcode.com/problems/count-common-words-with-one-occurrence/description/
    
    Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
    
    '''