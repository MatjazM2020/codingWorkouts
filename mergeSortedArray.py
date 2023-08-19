import copy
from typing import List

class Solution:
    def mergeHelper(self, arr: List[int],nums1: List[int], nums2: List[int], m: int, n:int, i:int, j:int, k: int)->List[int]:
        if i == m and j == n:
            return arr
        if i == m:
            arr[k] = nums2[j]
            return self.mergeHelper(arr,nums1,nums2,m,n,i,j+1,k+1)
        elif j == n:
            arr[k] = nums1[i]
            return self.mergeHelper(arr,nums1,nums2,m,n,i+1,j,k+1)
        elif nums1[i] <= nums2[j]: 
            arr[k] = nums1[i]
            return self.mergeHelper(arr,nums1,nums2,m,n,i+1,j,k+1)
        else: 
            arr[k] = nums2[j]
            return self.mergeHelper(arr,nums1,nums2,m,n,i,j+1,k+1)
                
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x = self.mergeHelper(copy.copy(nums1),nums1,nums2,m,n,0,0,0)
        for i in range(m+n):
            nums1[i] = x[i]

sol = Solution()
arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
sol.merge(arr1,3,arr2,3)
print(arr1)
                
        
        

        
        
#Exercise: https://leetcode.com/problems/merge-sorted-array/
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#The final sorted array should not be returned by the function, but instead 
#be stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
#where the first m elements denote the elements that should be merged, and the last n
#elements are set to 0 and should be ignored. nums2 has a length of n.
