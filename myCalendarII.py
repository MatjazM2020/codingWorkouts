class MyCalendarTwo:
    def __init__(self):
        self.singleBooked = []
        self.doubleBooked = []

    def book(self, start: int, end: int) -> bool:
        for a in self.doubleBooked:
            if a[1] > start and a[0] < end: 
                return False
        for a in self.singleBooked:
            if a[1] > start and a[0] < end:
                self.doubleBooked.append([max(a[0], start), min(a[1], end)])
        self.singleBooked.append([start, end])
        return True
    
'''
https://leetcode.com/problems/my-calendar-ii/description/

You are implementing a program to use as your calendar. We can add a new event if adding the event 
will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is
common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the
half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully 
without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
'''