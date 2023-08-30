from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: 
            return []
        res = []
        fst = 0
        lst = 0
        for i in range(1,len(nums)): 
            if nums[i] == nums[i-1]+1:
                lst = i
            else: 
                if lst - fst > 0: 
                    res.append(str(nums[fst]) + '->' + str(nums[lst]))
                else: 
                    res.append(str(nums[lst]))
                fst = i
                lst = i

        if lst - fst > 0: 
            res.append(str(nums[fst]) + '->' + str(nums[lst]))
        else: 
            res.append(str(nums[lst]))
        return res


#https://leetcode.com/problems/summary-ranges/
#You are given a sorted unique integer array nums.
#A range [a,b] is the set of all integers from a to b (inclusive).
#Return the smallest sorted list of ranges that cover all the numbers in the array 
# exactly. That is, each element of nums is covered by exactly one of the ranges, and
# there is no integer x such that x is in one of the ranges but not in nums.
#Each range [a,b] in the list should be output as:
#"a->b" if a != b , "a" if a == b
