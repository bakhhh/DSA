# Sohail Bakhshi 
# Student ID - 20605126
import unittest
from DSAStack import DSAStack 

capacity =100
class TestDSAStack(unittest.TestCase):

    def testPush(self):
        stack = DSAStack(capacity)
        for i in range(1, capacity):
            stack.push(i)
        

    def testIsEmpty(self):
        stack = DSAStack(capacity)
        self.assertEqual(stack.isEmpty(), True)
        for i in range(1, capacity):
            stack.push(i)
            self.assertEqual(stack.isEmpty(), False)

    def testIsFull(self):
        stack = DSAStack(capacity)
        for i in range(1, capacity):
            stack.push(i)
            if i > capacity:
                self.assertEqual(stack.isFull(), True)
            else:
                self.assertEqual(stack.isFull(), False)
    
    def testPop(self):
        stack = DSAStack(capacity)
        stack.push(1)
        stack.push(5)
        stack.push(3)
        stack.push(8)
        self.assertEqual(stack.pop(), 8 )
        stack.pop()
        self.assertEqual(stack.pop(), 5 )



    def testTop(self):
        stack = DSAStack(capacity)
        stack.push(1)
        self.assertEqual(stack.top(), 1)
        stack.push(4)
        self.assertEqual(stack.top(), 4)
        stack.push(10)
        self.assertEqual(stack.top(), 10)

    def testCount(self):
        stack = DSAStack(capacity)
        for i in range(10):
            stack.push(i)   
        self.assertEqual(stack.getCount(), 10)
        for i in range(20):
            stack.push(i)   
        self.assertEqual(stack.getCount(), 30)
        for i in range(10):
            stack.pop()   
        self.assertEqual(stack.getCount(), 20)


if __name__ == '__main__':
    unittest.main()