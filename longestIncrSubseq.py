class Solution:
    def lengthOfLIS(self, nums):
        if not nums: 
            return 0 
        n = len(nums)
        dp = [1 for _ in nums]

        for i in range(n): 
            for j in range(i): 
                if nums[i] > nums[j]: 
                    dp[i] = max(1+dp[j], dp[i])
        return max(dp)
    
    
    
    
#https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=dynamic-programming
#Given an integer array nums, return the length of the longest strictly increasing subsequence.