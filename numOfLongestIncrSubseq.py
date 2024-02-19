class Solution:
    def findNumberOfLIS(self, nums):
        if not nums: 
            return 0 
        n = len(nums)
        dp = [1 for _ in nums]
        n_dp = [1 for _ in nums]

        for i in range(n): 
            for j in range(i): 
                if nums[i] > nums[j]: 
                    if 1+dp[j] > dp[i]:
                        n_dp[i] = n_dp[j]
                    elif 1+dp[j] == dp[i]: 
                        n_dp[i] += n_dp[j]
                    dp[i] = max(1+dp[j], dp[i])
        max_val = max(dp)
        res = 0
        for i in range(n): 
            if dp[i] == max_val: 
                res += n_dp[i]
        return res
    
    
    
#https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#Given an integer array nums, return the number of longest increasing subsequences.
#Notice that the sequence has to be strictly increasing.

