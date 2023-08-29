class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,(len(s)//2)+1): 
            if len(s)%i == 0: 
                ss = s[:i]
                ae = ''
                for j in range(len(s)//i):
                    ae += ss
                if ae == s:
                    return True
        return False
        

#https://leetcode.com/problems/repeated-substring-pattern/
#Given a string s, check if it can be constructed by taking a substring of it 
#and appending multiple copies of the substring together.