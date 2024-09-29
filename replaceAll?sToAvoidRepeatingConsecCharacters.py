import string


class Solution:
    def modifyString(self, s: str) -> str:
        letters, n = set(string.ascii_lowercase), len(s)
        res = list(s)
        if res[0] == '?':
            if len(res) == 1: return 'a'
            if res[1] == '?': res[0] = 'a'
            else:
                for c in letters:
                    if res[1] != c:
                        res[0] = c
                        break

        for i in range(1,n-1):
            if res[i] == '?':
                for c in letters:
                    if c != res[i-1] and c!= res[i+1]:
                        res[i] = c
                        break
        
        if res[n-1] == '?':
            if res[n-2] == '?': res[n-2] = 'a'
            else:
                for c in letters:
                    if res[n-2] != c:
                        res[n-1] = c
                        break
        return res



'''
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description/

Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase 
letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return 
any of them. It can be shown that an answer is always possible with the given constraints.
'''