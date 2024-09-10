from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0]*1000
        for ppl, s, e in trips:
            for l in range(s,e):
                timeline[l] += ppl
                if timeline[l] > capacity: return False
        return True
                             
'''
https://leetcode.com/problems/car-pooling/description/

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] 
indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off
are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's
initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.
'''