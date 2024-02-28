import heapq

class Solution:
    def maxProduct(self, nums):
        res = heapq.nlargest(2,nums)
        return (res[0]-1)*(res[1]-1)




#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
#Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).