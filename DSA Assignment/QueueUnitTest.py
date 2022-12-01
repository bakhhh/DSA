#File: #QueueUnitTest.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 4/4/22
#Data Structures & Algorithms Assignment
##DSAQueueTest has been reused and modified from prac3 
#Previously submitted for Practical 3,4 in COMP1002, Sem 2, 2022
import unittest
from DSAQueue import *

capacity =100
#Testing Queue
class TestDSAQueue(unittest.TestCase):

#testing if queue is empty
    def testIsEmpty(self):
        queue = DSAQueue()
        self.assertEqual(queue.isEmpty(), True)
        for i in range(1, capacity):
            queue.enqueue(i)
            self.assertEqual(queue.isEmpty(), False)

#testing if queue is full
    def testIsFull(self):
        queue = DSAQueue()
        for i in range(1, 101):
            queue.enqueue(i)
            if i > capacity:
                self.assertEqual(queue.isFull(), True)
            elif i < capacity:
                self.assertEqual(queue.isFull(), False)

#testing peek
    def testPeek(self):
        queue = DSAQueue()
        queue.enqueue(2)
        queue.enqueue(4)
        queue.enqueue(5)
        queue.enqueue(6)
        self.assertEqual(queue.isEmpty(), False)
        self.assertEqual(queue.peek(), 2)
        queue.dequeue()
        self.assertEqual(queue.peek(), 4)
        queue.dequeue()
        self.assertEqual(queue.peek(), 5)
        queue.dequeue()
        self.assertEqual(queue.peek(), 6)
        queue.dequeue()
        self.assertEqual(queue.isEmpty(), True)
       
#testing the count    
    def testGetCount(self):
        queue = DSAQueue()
        for i in range(10):
            queue.enqueue(i+1)
        self.assertEqual(queue.getCount(), 10)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.getCount(), 9)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.getCount(), 8)

#testing enqueue
    def testEnqueue(self):
        queue = DSAQueue()
        self.assertEqual(queue.enqueue(1),1)
        self.assertEqual(queue.enqueue(9),9)
        self.assertEqual(queue.enqueue(3),3)
        self.assertEqual(queue.enqueue(5),5)
        self.assertEqual(queue.enqueue(10),10)
        self.assertEqual(queue.count,5)

#testing dequeue
    def testDequeue(self):
        queue = DSAQueue()
        queue.enqueue(1)
        queue.enqueue(9)
        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(10)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 9)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 10)


if __name__ == '__main__':
    unittest.main()