#File: #DSAQueue.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 3/4/22
#Data Structures & Algorithms Assignment
#Previously submitted for Practical 4 in COMP1002, Sem 2, 2022
#Updated version of DSAQueue that uses linked lists
from DSALinkedLists import *
from myException import * #FYI valueError is my own class 

#Queue class
class DSAQueue:

    def __init__(self):
        self.capacity = 100 #the max amount of values it can hold
        self.count = 0  #counts how much items are in the list
        self.queue = DSALinkedList()

#Method: getCount
#function that returns count 
    def getCount(self): 
        return self.count 

#Method: isEmpty
#checks if empty returns true if empty
    def isEmpty(self) :
        isEmpty = False
        if self.count == 0:
            isEmpty=True
        return isEmpty

#Method: isFull   
#checks if full returns true if full     
    def isFull(self): 
        isFull = False
        if self.count == self.capacity:
            isFull=True
        return isFull

#Method: peek
#returns first value in queue
    def peek(self): 
        return self.queue.peekFirst()

#Method: enqueue
#adds to the queue
    def enqueue(self,value): 
        try:
            if (self.isFull()):
                raise valueError("Queue is full ")
            else:
                self.queue.insertLast(value)
                self.count+=1
            return value
        except valueError as e:
            print(e)

#Method: dequeue
#removes from the queue
    def dequeue(self): 
        firstVal = self.queue.peekFirst() # first value
        if self.count != self.isEmpty(): #if not empty
            self.queue.removeFirst()
        self.count -=1
        return firstVal

#Method: display
#displays whats in the queue
    def display(self): 
        for i in self.queue:
            print(i, end ='')
        print('')

