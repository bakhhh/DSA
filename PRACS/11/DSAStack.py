# prac 11 stack
from collections import deque

class DSAStack:
    def __init__(self):
        self.capacity = 100
        self.count = 0 
        self.stack = deque()

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
            self.stack.append(value)
            self.count +=1

    def pop(self):
        self.count -=1
        return self.stack.pop()

    def top(self):
        return self.stack[self.count-1]
     
