class SnapshotArray:
    def __init__(self, length: int):   
        self.snap_id = 0
        self.snapshots = [[(0, 0)] for i in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.snap_id == self.snapshots[index][-1][0]:
            self.snapshots[index][-1] = (self.snap_id, val)
        else:
            self.snapshots[index].append((self.snap_id, val))
            
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id-1
    
    def get(self, index: int, snap_id: int) -> int:
        snaps = self.snapshots[index]
        l, r, cap = 0, len(snaps)-1, 0
        while l <= r: 
            c = (l+r)//2
            if snaps[c][0] < snap_id:
                l = c + 1
                cap = snaps[c][1]
            elif snaps[c][0] > snap_id:
                r = c - 1
            else:
                return snaps[c][1]
        return cap

    
    
'''
https://leetcode.com/problems/snapshot-array/?envType=study-plan-v2&envId=binary-search
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
'''