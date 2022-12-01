#File: #DSAHeap.py
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 30/9/22
#Data Structures & Algorithms Assignment
import unittest
import numpy as np

class DSAHeap:
    def __init__(self,size):
        self.count = 0
        self.heapArray = np.zeros(size,dtype=object)
        self.size = size

    def add(self,priority,value):
        try:
            if self.isFull()==True:
                raise ValueError("Heap is full")
            else:
                self.heapArray[self.count] = DSAHeapEntry(priority,value)
                self.trickleUp(self.count)
                self.count += 1
        except Exception as e:
            print(e)

    def isFull(self):
        isFull =False
        if self.count==self.size:
            isFull =True
        return isFull

    def isEmpty(self):
        isEmpty =False
        if self.count==0:
            isEmpty =True
        return isEmpty

    def remove(self):
        try:
            if self.isEmpty()==True:
                raise ValueError("Cant remove as heap is Empty")
            else:
                root = self.heapArray[0]
                self.count -= 1
                self.heapArray[0] = self.heapArray[self.count]
                self.trickleDown(0,self.count)
                return root
        except Exception as e:
            print(e)

    def display(self):
        for i in range(self.count):
            print(self.heapArray[i].priority)
        print('')
    

    def swap(self,largeIdx,curIdx):
        self.heapArray[largeIdx], self.heapArray[curIdx] = self.heapArray[curIdx],self.heapArray[largeIdx]

    def trickleUp(self,curIdx):
        parentIdx = (curIdx-1)//2
        if curIdx > 0:
            if self.heapArray[curIdx].getPriority() > self.heapArray[parentIdx].getPriority():
                self.swap(parentIdx, curIdx)
                self.trickleUp(parentIdx)


    def trickleDown(self,curIdx,numItems): #recursive solution would give wrong output in heapsort

        left = (curIdx * 2) + 1
        right = (curIdx * 2) + 2
        keepGoing = True

        while keepGoing==True and left<numItems:
            largeIdx = left
            if right < numItems:
                if self.heapArray[left].getPriority() < self.heapArray[right].getPriority():
                    largeIdx = right
            if self.heapArray[largeIdx].getPriority() > self.heapArray[curIdx].getPriority():
                self.swap(largeIdx, curIdx)
                keepGoing = True
            curIdx = largeIdx
            left = (curIdx * 2) + 1
            right = (curIdx *2) + 2
            
    def heapify(self):
        for i in range((self.count//2)-1):
            self.trickleDown(i, self.count)

    def heapSort(self):
        self.heapify()
        for i in range(self.count-1, 0, -1):
            self.swap(0, i)
            self.trickleDown(0, i)
   

class DSAHeapEntry:
    def __init__(self,priority,value):
        self.priority = priority
        self.value = value
    
    def getPriority(self):
        return self.priority

    def setPriority(self,priority):
        self.priority= priority

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value =value



class TestHeap(unittest.TestCase):
    def testHeap(self):
        heap = DSAHeap(10)
        heap.add(1,1)
        heap.add(2,2)
        heap.add(3,3)
        heap.add(4,4)
        heap.add(5,5)
        heap.add(6,6)
        heap.remove()

        # heap.heapSort()
        heap.display()




if __name__ == "__main__":
    unittest.main()