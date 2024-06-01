from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict: 
            v = self.dict[key]
            self.dict.pop(key)
            self.dict[key] = v
            return self.dict[key]
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.dict) >= self.capacity:
            self.dict.popitem(last= False)
        if key in self.dict: 
            self.dict.pop(key)
            self.dict[key] = value
        else: 
            self.dict[key] = value                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
https://leetcode.com/problems/lru-cache/description/
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''