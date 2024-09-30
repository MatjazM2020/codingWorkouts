class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = [-1]*maxSize
        self.top = 0
        
    def push(self, x: int) -> None:
        if self.top < self.maxSize: 
            self.stack[self.top] = x
            self.top += 1

    def pop(self) -> int:
        if self.top == 0:
            return -1
        top = self.top
        self.top -= 1
        return self.stack[self.top]
        

    def increment(self, k: int, val: int) -> None:
        if self.top < k:
            for i in range(self.top):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)









'''

https://leetcode.com/problems/design-a-stack-with-increment-operation/

Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.

'''