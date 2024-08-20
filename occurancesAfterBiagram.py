from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        arr = text.split()
        n = len(arr)
        res = []
        for i in range(n-2):
            if arr[i] == first and arr[i+1] == second:
                res.append(arr[i+2])
        return res



'''
https://leetcode.com/problems/occurrences-after-bigram/

Given two strings first and second, consider occurrences in some text of the form
"first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".

'''