from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = {}
        for (id,time) in logs:
            if id not in users:
                users[id] = {time}
            else:
                users[id].add(time)
        answer = [0 for _ in range(k)]
        for id in users:
            answer[len(users[id])-1] += 1
        return answer
    
    
    
'''
https://leetcode.com/problems/finding-the-users-active-minutes/description/

You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs 
where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action
on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of
users whose UAM equals j.

Return the array answer as described above.

'''