# Sohail Bakhshi 
# Student ID - 20605126
#Previously submitted for Practical 4 in COMP1002, Sem 2, 2022
#
from numpy import ndarray
from linkedLists import *

class DSAQueue:

    def __init__(self):
        self.capacity = 100
        self.count = 0
        self.queue = DSALinkedList()
    
    def getCount(self):
        return self.count

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity

    def peek(self):
        return self.queue.peekFirst()

    def enqueue(self,value):
        if (self.isFull()):
            raise ValueError("Queue is full ")
        else:
            self.queue.insertLast(value)
            self.count+=1
        return value

    def dequeue(self):
        firstVal = self.queue.peekFirst() # first value
        if self.count != self.isEmpty(): #if not empty
            self.queue.removeFirst()
        self.count -=1
        return firstVal


