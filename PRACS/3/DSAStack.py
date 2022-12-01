# Sohail Bakhshi 
# Student ID - 20605126
import numpy as np

class DSAStack:
    def __init__(self, DEFAULT_CAPACITY=100):
        self.capacity = DEFAULT_CAPACITY
        if self.capacity < 0:
            raise ValueError("Capacity Cant be negative ")
        self.count = 0 
        self.stack = np.ndarray(self.capacity, dtype= object)
        
    def getCount(self):
        return self.count
        
    def isEmpty(self) -> bool:
        if self.count ==0:
            return True
        else: 
            return False
        
             
    def isFull(self)-> bool:
        if self.count == self.capacity:
            return True
        else:
            return False
        
    def push(self, value):
        if self.isFull()== True:
            raise ValueError("Stack is full")
        else:
            self.stack[self.count] = value
            self.count +=1

    def pop(self):
        topval = self.top()
        self.count -= 1
        return topval

    def top(self):
        if not self.isEmpty():
            return self.stack[self.count -1]
        
            
    def display(self): # display callstack
        stack = self.stack[:self.count]
        for line in stack:
            print("%s" % line)

# stack = DSAStack(100)


# push = stack.push(20)
# push = stack.push(10)
# count = stack.getCount()
# top = stack.top()
# full = stack.isFull()
# empty = stack.isEmpty()
# pop = stack.pop()


# print(push)

