class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def convert(sr):
            res, n = [], len(sr)
            for i in range(n):
                res += str(ord(sr[i]) - ord('a') + 1)
            return res

        def sumUp(sr):
            res, n = 0, len(sr)
            for i in range(n):
                res += int(sr[i])
            return str(res)
        
        s = convert(s)
        while k > 0:
            s = sumUp(s)
            k -= 1
        return int(s)


'''
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03

You are given a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 
'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform 
operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.

'''
