#prac 11 deque

from collections import deque

class DSAQueue:

    def __init__(self):
        self.capacity = 100
        self.count = 0
        self.queue = deque()

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

    def peek(self):
        return self.queue[0]

    def enqueue(self,value):
        retVal = self.queue.append(value)
        self.count+=1
        return retVal

    def dequeue(self):
        retVal = self.queue.popleft()
        self.count-=1
        return retVal
