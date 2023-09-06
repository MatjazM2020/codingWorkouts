from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        a = 1
        num = num_people
        stash = candies
        people = [0]*num
        while stash > 0: 
            if stash - a > 0: 
                people[(a-1)%num] += a
                stash -= a
            else:
                people[(a-1)%num] += stash
                stash = 0
                break
            a += 1
        return people
        
        
        
        
#https://leetcode.com/problems/distribute-candies-to-people/
#We distribute some number of candies, to a row of n = num_people people in the following way:
#We then give 1 candy to the first person, 2 candies to the second person, and so on until we give
# n candies to the last person.
#Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies 
# to the second person, and so on until we give 2 * n candies to the last person.
#This process repeats (with us giving one more candy each time, and moving to the start of the row 
# after we reach the end) until we run out of candies.  The last person will receive all of our 
# remaining candies (not necessarily one more than the previous gift).
#Return an array (of length num_people and sum candies) that represents the final distribution of 
# candies.

