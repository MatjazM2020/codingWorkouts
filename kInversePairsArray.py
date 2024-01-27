class Solution(object):
    def helper(self,n,k,memo):
        if (n,k) in memo: 
            return memo[(n,k)]
        if n == 1 and k == 0: 
            return 1 
        elif n < 0 or k < 0 or k > n*(n-1)/2:
            return 0 
        else: 
            memo[(n,k)] = (self.helper(n,k-1,memo) + self.helper(n-1,k,memo) - self.helper(n-1,k-n,memo))%((10**9)+7)
            return memo[(n,k)]
    def kInversePairs(self, n, k):
        return self.helper(n,k,{})


#https://leetcode.com/problems/k-inverse-pairs-array/description/?envType=daily-question&envId=2024-01-27
#For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].
#Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly 
# k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.
