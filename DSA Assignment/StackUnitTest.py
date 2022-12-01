#File: #StackUnitTest.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 4/4/22
#Data Structures & Algorithms Assignment
##DSAStackTest has been reused and modified from prac3 
#Previously submitted for Practical 3 in COMP1002, Sem 2, 2022
import unittest
from DSAStack import DSAStack 

capacity =100
#testing stack
class TestDSAStack(unittest.TestCase):

#testing if i can push
    def testPush(self):
        stack = DSAStack()
        self.assertEqual(stack.push(1),1)  
        self.assertEqual(stack.push(2),2)  
        self.assertEqual(stack.push(3),3)  
        self.assertEqual(stack.push(4),4)  
        self.assertEqual(stack.push(5),5)  

#testing if stack is empty
    def testIsEmpty(self):
        stack = DSAStack()
        self.assertEqual(stack.isEmpty(), True)
        for i in range(1, capacity):
            stack.push(i)
            self.assertEqual(stack.isEmpty(), False)

#testing if stack is full
    def testIsFull(self):
        stack = DSAStack()
        for i in range(1, capacity):
            stack.push(i)
            if i > capacity:
                self.assertEqual(stack.isFull(), True)
            else:
                self.assertEqual(stack.isFull(), False)

#testing if i can pop/remove
    def testPop(self):
        stack = DSAStack()
        stack.push(1)
        stack.push(5)
        stack.push(3)
        stack.push(8)
        self.assertEqual(stack.pop(), 8 )
        stack.pop()
        self.assertEqual(stack.pop(), 5 )

#testing if it returns the top value
    def testTop(self):
        stack = DSAStack()
        stack.push(1)
        self.assertEqual(stack.top(), 1)
        stack.push(4)
        self.assertEqual(stack.top(), 4)
        stack.push(10)
        self.assertEqual(stack.top(), 10)

#testing if count is correct
    def testCount(self):
        stack = DSAStack()
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