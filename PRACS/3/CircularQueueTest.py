# Sohail Bakhshi 
# Student ID - 20605126
import unittest
from DSAQueue import CircularQueue

capacity =100
class TestCircularQueue(unittest.TestCase):

    def testIsEmpty(self):
        queue = CircularQueue(capacity)
        self.assertEqual(queue.isEmpty(), True)
        for i in range(1, capacity):
            queue.enqueue(i)
            self.assertEqual(queue.isEmpty(), False)
    
    def testIsFull(self):
        queue = CircularQueue(capacity)
        for i in range(1, capacity):
            queue.enqueue(i)
            if i > capacity:
                self.assertEqual(queue.isFull(), True)
            else:
                self.assertEqual(queue.isFull(), False)

    def testPeek(self):
        queue = CircularQueue(capacity)
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
        queue = CircularQueue(capacity)
        for i in range(10):
            queue.enqueue(i+1)
        self.assertEqual(queue.getCount(), 10)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.getCount(), 9)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.getCount(), 8)
   
    def testEnqueue(self):
        queue = CircularQueue(capacity)
        for i in range(capacity):
            queue.enqueue(i)

    def testDequeue(self):
        queue = CircularQueue(capacity)
        queue.enqueue(1)
        queue.enqueue(9)
        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(10)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 9)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 5)





if __name__ == '__main__':
    unittest.main()


