from typing import List
import copy
from collections import OrderedDict

class Solution:
    def delHelper(self, nums:List[int], dict:dict) -> int: 
        if len(dict) > 3:
            dict[list(dict)[2]] +=  dict[list(dict)[0]]
            for i in range(3,len(dict)):
                if dict[list(dict)[i-2]] >= dict[list(dict)[i-3]]:
                    dict[list(dict)[i]] +=  dict[list(dict)[i-2]]
                else: 
                    dict[list(dict)[i]] +=  dict[list(dict)[i-3]]
        elif len(dict) == 3: 
            return max(dict[list(dict)[0]] + dict[list(dict)[2]], dict[list(dict)[1]])
        elif len(dict) == 2: 
            return max(dict[list(dict)[0]], dict[list(dict)[1]])
        elif len(dict) == 1:
            return dict[list(dict)[0]]
        else:
            return sum
        return max(dict[list(dict)[len(dict)-1]], dict[list(dict)[len(dict)-2]])
        
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = {}
        sum = 0
        result = 0
        for x in nums: 
            try: 
                d[x] += x
            except: 
                d[x] = x
        rem = []
        for a in d:
            if not(a-1 in d) and not(a+1 in d): 
                sum += d[a]
                rem.append(a)
        for x in rem: 
            d.pop(x)
        d = OrderedDict(sorted(d.items()))
        
        k = 0
        for i in range(1,len(d)): 
            if list(d)[i-1]+1 == list(d)[i]:
                if i == len(d)-1: 
                    temp = dict(list(d.items())[k:i+1])
                    result += self.delHelper(nums,temp)
                pass
            else:
                temp = dict(list(d.items())[k:i])
                result += self.delHelper(nums,temp)
                k = i                 
        return result+sum
            


#https://leetcode.com/problems/delete-and-earn/?envType=study-plan-v2&envId=dynamic-programming
#You are given an integer array nums. You want to maximize the number of points you get by performing
# the following operation any number of times:
#Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to 
# nums[i] - 1 and every element equal to nums[i] + 1. Return the maximum number of points you can earn by 
# applying the above operation some number of times.