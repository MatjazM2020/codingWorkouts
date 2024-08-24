class Solution:
    def nearestPalindromic(self, n: str) -> str:
        sz = len(n)
        l = len(n)//2
        candidates = set()

        stInt = int(n)
        if stInt < 10 and stInt > 0:
            return str(stInt-1)
        elif stInt == 0:
            return '1'

        candidates.add(int('9'*(sz-1)))
        candidates.add(int('1'+'0'*(sz-1)+'1'))

        def isPalindrome():
            return n == n[::-1]

        def mirrorLeft(left, mid = None):
            if mid:
                candidates.add(int(left + mid + left[::-1]))
            else:
                candidates.add(int(left + left[::-1]))

        if sz%2 == 0:
            if not isPalindrome(): mirrorLeft(n[:l])
            mirrorLeft(str(int(n[:l])-1))
            mirrorLeft(str(int(n[:l])+1))
        else:
            if not isPalindrome(): mirrorLeft(n[:l], n[l])
            if int(n[l]) > 0: 
                mirrorLeft(n[:l], str(int(n[l])-1))
                mirrorLeft(n[:l], str(int(n[l])+1))
            elif int(n[l]) == 0: mirrorLeft(n[:l], '1')
            mirrorLeft(str(int(n[:l])-1), n[l])
            mirrorLeft(str(int(n[:l])+1), n[l])
        
        minDiff = float('inf')
        prevVal = None
        for x in candidates:
            if x == stInt:
                continue
            diff = abs(x - stInt)
            if diff < minDiff or (diff == minDiff and x < prevVal):
                minDiff = diff
                prevVal = x

        return str(prevVal)
    
'''
https://leetcode.com/problems/find-the-closest-palindrome/description/?envType=daily-question&envId=2024-08-24

Given a string n representing an integer, return the closest integer (not including itself), 
which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

'''