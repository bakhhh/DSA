# Sohail Bakhshi 
# Student ID - 20605126
from numpy import ndarray

class DSAQueue:

    def __init__(self, DEFAULT_CAPACITY):
        self.capacity = DEFAULT_CAPACITY
        self.count = 0
        self.queue = ndarray(self.capacity, dtype=object)
        self.head, self.tail = 0, 0
    
    def getCount(self):
        return self.count

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity

    def peek(self):
        return self.queue[self.head]

    def enqueue(self,value):
         pass

    def dequeue(self):
        pass


class ShufflingQueue(DSAQueue):
    def __init__(self, DEFAULT_CAPACITY):
        super().__init__(DEFAULT_CAPACITY)

    def enqueue(self,value):
        if (self.isFull()):
            raise ValueError("Queue is full ")
        else:
            self.queue[self.count] = value
            self.count+=1
        return value

    def dequeue(self):
        firstVal = self.queue[0] # first value
        if self.count != self.isEmpty(): #if not empty
            for i in range(len(self.queue)): # looping through the queue
                self.queue[i-1] = self.queue[i] # shuffling the values up the queue

        self.count -=1
        return firstVal
    
class CircularQueue(DSAQueue):
    
    def __init__(self, DEFAULT_CAPACITY):
        super().__init__(DEFAULT_CAPACITY)
        
    def enqueue(self,value):
        if (self.isFull()):
            raise ValueError("Queue is full ")
        else:
            self.count +=1
            self.queue[self.tail] = value
            self.tail = (self.tail +1) % self.capacity
        return value
        
    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Queue is empty ")
        else:
            self.count -=1
            value = self.queue[self.head]
            self.head = (self.head +1) %self.capacity 
        return value

  