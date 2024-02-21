class Solution:
    def longestArithSeqLength(self, nums):
        if not nums: 
            return 0 
        n = len(nums)
        dp = defaultdict(dict)
        res = 1 

        for i in range(n): 
            for j in range(i): 
                diff = nums[i]-nums[j]
                if diff not in dp[j]: 
                    dp[j][diff] = 1
                if diff not in dp[i]:
                    dp[i][diff] = 1
                
                dp[i][diff] = dp[j][diff] +1 
                res = max(res, dp[i][diff])
        return res



#https://leetcode.com/problems/longest-arithmetic-subsequence/description/?envType=study-plan-v2&envId=dynamic-programming
#Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
#Note that:
#A subsequence is an array that can be derived from another array by deleting some or no elements without changing 
# the order of the remaining elements. A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value 
# (for 0 <= i < seq.length - 1).
