#File: #DSAStack.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 3/4/22
#Data Structures & Algorithms Assignment
#Previously submitted for Practical 3 in COMP1002, Sem 2, 2022
import numpy as np
from myException import * #FYI valueError is my own class 

#stack class
class DSAStack:
    def __init__(self):
        self.capacity = 100 #the max amount of values it can hold
        self.count = 0 #counts how much items are in the list
        self.stack = np.ndarray(self.capacity, dtype= object)

#Method: getCount
#function that returns count 
    def getCount(self): #function that returns count
        return self.count

#Method: isEmpty
#checks if empty returns true if empty
    def isEmpty(self): #checks if empty returns true if empty
        isEmpty = False
        if self.count == 0:
            isEmpty=True
        return isEmpty

#Method: isFull
#checks if full returns true if empty 
    def isFull(self): #checks if full returns true if full
        isFull = False
        if self.count == self.capacity:
            isFull=True
        return isFull
        
#Method: push
#adds to the stack
    def push(self, value): #adds to the stack
        try:
            if self.isFull()== True:
                raise valueError("Stack is full")
            else:
                self.stack[self.count] = value
                self.count +=1
            return value
        except valueError as e:
            print(e)

#Method: push
#removes top value from stack
    def pop(self): 
        topval = self.top()
        self.count -= 1
        return topval

#Method: push
#returns the top value
    def top(self): 
        if not self.isEmpty():
            return self.stack[self.count -1]

#Method: display
# displays items in stack          
    def display(self): 
        stack = self.stack[:self.count]
        for line in stack:
            print(line, end =' ')
        print("")
