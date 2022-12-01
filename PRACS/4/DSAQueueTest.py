# Sohail Bakhshi 
# Student ID - 20605126
##DSAQueueTest has been reused and modified from prac3 

import unittest
from DSAQueue import *

capacity =100
class TestQueue(unittest.TestCase):

    def testIsEmpty(self):
        queue = DSAQueue(capacity)
        self.assertEqual(queue.isEmpty(), True)
        for i in range(1, capacity):
            queue.enqueue(i)
            self.assertEqual(queue.isEmpty(), False)
    
    def testIsFull(self):
        queue = DSAQueue(capacity)
        for i in range(1, 101):
            queue.enqueue(i)
            if i > capacity:
                self.assertEqual(queue.isFull(), True)
            elif i < capacity:
                self.assertEqual(queue.isFull(), False)

    def testPeek(self):
        queue = DSAQueue(capacity)
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

        
        
    def testCount(self):
        queue = DSAQueue(capacity)
        for i in range(10):
            queue.enqueue(i+1)
        self.assertEqual(queue.getCount(), 10)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.getCount(), 9)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.getCount(), 8)
   
    def testEnqueue(self):
        queue = DSAQueue(capacity)
        for i in range(capacity):
            queue.enqueue(i)

    def testDequeue(self):
        queue = DSAQueue(capacity)
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