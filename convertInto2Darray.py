class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        marked = [False for _ in range(n)] 
        res = []
        counter = 0 

        while counter < n:
            cur = [] 
            for i in range(n):
                if not marked[i] and nums[i] not in cur: 
                    cur.insert(-1, nums[i])  
                    marked[i] = True
                    counter += 1
            res.insert(-1, cur)
        return res




#https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
# Note that the 2D array can have a different number of elements on each row.
