# Sohail Bakhshi 
# Student ID - 20605126
#Previously submitted for Practical 3 in COMP1002, Sem 2, 2022
#
from numpy import ndarray
from linkedLists import *

class DSAQueue:

    def __init__(self, DEFAULT_CAPACITY):
        self.capacity = DEFAULT_CAPACITY
        self.count = 0
        self.queue = DSALinkedList()
        self.head, self.tail = 0, 0
    
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


  