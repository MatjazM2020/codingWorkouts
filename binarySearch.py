class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1 
        while left <= right: 
            mid = left + (right-left)//2
            if nums[mid] == target: 
                return mid 
            elif target > nums[mid]: 
                left = mid + 1 
            else: 
                right = mid - 1 
        return -1 



#https://leetcode.com/problems/binary-search/description/?envType=study-plan-v2&envId=binary-search
#Given an array of integers nums which is sorted in ascending order, and an integer target, write a
# function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.