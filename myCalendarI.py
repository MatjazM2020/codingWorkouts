class MyCalendar:

    def __init__(self):
        self.intervals = []
    
    def book(self, start: int, end: int) -> bool:
        for interval in self.intervals:
            if interval[1] > start and interval[0] < end:
                return False
        self.intervals.append([start, end])
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
    
    
    
    
    
'''
https://leetcode.com/problems/my-calendar-i/description/
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end),
the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking.
Otherwise, return false and do not add the event to the calendar.
'''