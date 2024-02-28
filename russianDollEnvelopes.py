class Solution: 
    def maxEnvelopes(self, envelopes): 
        n = len(envelopes)
        envelopes = sorted(envelopes, key = lambda x: (x[0],-x[1])) 
        dp = [envelopes[0][1]]
        
        for i in range(1,n):
            height = envelopes[i][1]
            if dp[-1] < height: 
                dp.append(height)
            else: 
                left, right = 0, len(dp)
                while left < right: 
                    mid = left + (right-left)//2
                    if dp[mid] < height: 
                        left = mid + 1
                    else: 
                        right = mid 
                dp[left] = height
        return len(dp)        




#https://leetcode.com/problems/russian-doll-envelopes/description/?envType=study-plan-v2&envId=dynamic-programming

#You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the
# height of an envelope. One envelope can fit into another if and only if both the width and height of one
# envelope are greater than the other envelope's width and height. Return the maximum number of envelopes
# you can Russian doll (i.e., put one inside the other). 
# note: You cannot rotate an envelope.