class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        max = 1
        pair = [0,0]
        x = [[0 for _ in range(l)] for _ in range(l)]
        for i in range(l): 
            x[i][i] = 1
        for i in range(l-1): 
            if(s[i] == s[i+1]): 
                x[i][i+1] = 2
                max = 2
                pair = [i,i+1]
        
        for j in range(2,l): 
            indx = [0,j]
            for i in range(l-j): 
                if x[indx[0]+1][indx[1]-1]>0 and s[indx[0]]==s[indx[1]]: 
                    x[indx[0]][indx[1]] = x[indx[0]+1][indx[1]-1] + 2 
                    if x[indx[0]][indx[1]]> max:
                        max = x[indx[0]][indx[1]]
                        pair = [indx[0],indx[1]]
                else:
                    x[indx[0]][indx[1]] = 0
                indx[0] += 1
                indx[1] += 1 
        return s[pair[0]:pair[1]+1]
    

#https://leetcode.com/problems/longest-palindromic-substring/?envType=study-plan-v2&envId=dynamic-programming
#Given a string s, return the longest palindromic substring in s.