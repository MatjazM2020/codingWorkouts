class TimeMap:
    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [(timestamp, value)]
        else: 
            self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
            if key not in self.dict:
                return ""
            n = len(self.dict[key])
            l, r = 0, n-1
            capture = 0
            while l <= r:
                c = (l+r)//2
                x = self.dict[key][c][0]
                capture = self.dict[key][c][1]
                if x < timestamp: 
                    if c == n-1:
                        return capture
                    l = c + 1
                elif x > timestamp:
                    if c == 0:
                        return ""
                    r = c - 1
                    capture = self.dict[key][c-1][1]
                else:
                    return capture
            return capture


'''
https://leetcode.com/problems/time-based-key-value-store/description/?envType=study-plan-v2&envId=binary-search
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve
the key's value at a certain timestamp.

Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
'''