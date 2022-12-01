# Sohail Bakhshi 
# Student ID - 20605126
#Previously submitted for Practical 3 in COMP1002, Sem 2, 2022
import numpy as np
from linkedLists import *

class DSAStack:
    def __init__(self, DEFAULT_CAPACITY=100):
        self.capacity = DEFAULT_CAPACITY
        if self.capacity < 0:
            raise ValueError("Capacity Cant be negative ")
        self.count = 0 
        self.stack = DSALinkedList()

    def __iter__(self):
        return iter(DSAStack)
        
    def getCount(self):
        return self.count
        
    def push(self, value):
        if not self.isFull():
            self.stack.insertLast(value)
            self.count +=1
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            topval = self.top()
            self.count -= 1
            self.stack.removeLast()
        return topval

    def top(self):
        if not self.isEmpty():
            return self.stack.peekLast()
        
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