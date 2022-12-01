import unittest
from DSATree import *


class TestBST(unittest.TestCase):
    def testInsert(self):
        tree = BinarySearchTree()
        tree.insert(10, "ten")
        tree.insert(20, "twenty")
        tree.insert(30, "thirty")
        tree.insert(40, "fourty")
        self.assertEqual(tree.find(10), "ten")
        self.assertEqual(tree.find(20), "twenty")
        self.assertEqual(tree.find(30), "thirty")
        self.assertEqual(tree.find(40), "fourty")

    def testHeight(self):
        tree = BinarySearchTree()
        self.assertEqual(tree._height(), -1)
        tree.insert(10, "ten")
        self.assertEqual(tree._height(), 0)
        tree.insert(5, "five")
        tree.insert(30, "thirty")
        self.assertEqual(tree._height(), 1)
        tree.insert(1, "one")
        tree.insert(20, "twenty")
        tree.insert(40, "fourty")
        self.assertEqual(tree._height(), 2)
        tree.insert(100, "One hundred")
        self.assertEqual(tree._height(), 3)
        tree.insert(50, "Fifty")
        self.assertEqual(tree._height(), 4)
        tree.insert(77, "Seventy Seven")
        self.assertEqual(tree._height(), 5)

       
        
    def testMin(self):
        tree = BinarySearchTree()
        tree.insert(10, "ten")
        tree.insert(20, "twenty")
        tree.insert(30, "thirty")
        tree.insert(40, "fourty")
        tree.insert(1, "fourty")
        self.assertEqual(tree.min(), 1)

    def testMax(self):
        tree = BinarySearchTree()
        tree.insert(10, "ten")
        tree.insert(20, "twenty")
        tree.insert(30, "thirty")
        tree.insert(40, "fourty")
        tree.insert(1, "one")
        tree.insert(100, "One hundred")
        tree.insert(50, "Fifty")
        tree.insert(77, "Seventy Seven")
        self.assertEqual(tree.max(), 100)

    def testDelete(self):
        tree = BinarySearchTree()
        tree.insert(4, "D")
        tree.insert(2, "B")
        tree.insert(6, "F")
        tree.insert(1, "A")
        tree.insert(3, "C")
        tree.insert(5, "E")
        tree.insert(7, "G")
        print(tree.inorder())
        tree.delete(4)
     
        print(tree.inorder())
       

        


if __name__ == "__main__":
    unittest.main()
