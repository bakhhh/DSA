#File: #LinkedListUnitTest.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 4/4/22
#Data Structures & Algorithms Assignment
#Previously submitted for Practical 4 in COMP1002, Sem 2, 2022
import unittest
from DSALinkedLists import *
#Linked List Test
class TestDSALinkedList(unittest.TestCase):

#testing insert functions and checking if its within the list
    def testInsert(self):
        ll = DSALinkedList()
        ll.insertFirst("a")
        ll.insertLast("b")
        ll.insertLast("c")
        ll.insertLast("d")
        self.assertEqual(ll.checkFind("a"), True)
        self.assertEqual(ll.checkFind("b"), True)
        self.assertEqual(ll.checkFind("c"), True)
        self.assertEqual(ll.checkFind("d"), True)
        self.assertEqual(ll.checkFind("e"), False)

#testing if remove first works
    def testRemoveFirst(self):
        ll = DSALinkedList()
        ll.insertFirst("a")
        ll.insertFirst("b")
        ll.insertFirst("c")
        ll.insertFirst("d")
        self.assertEqual(ll.removeFirst(), "d")
        self.assertEqual(ll.removeFirst(), "c")
        self.assertEqual(ll.removeFirst(), "b")
        self.assertEqual(ll.removeFirst(), "a")
        self.assertEqual(ll.isEmpty(), True)

#testing if remove last works
    def testRemoveLast(self):
        ll = DSALinkedList()
        ll.insertLast("a")
        ll.insertLast("b")
        ll.insertLast("c")
        ll.insertLast("d")
        self.assertEqual(ll.removeLast(), "d")
        self.assertEqual(ll.checkFind("d"), False)
        self.assertEqual(ll.removeLast(), "c")
        self.assertEqual(ll.checkFind("c"), False)
        self.assertEqual(ll.removeLast(), "b")
        self.assertEqual(ll.checkFind("b"), False)
        self.assertEqual(ll.removeLast(), "a")
        self.assertEqual(ll.checkFind("a"), False)
        self.assertEqual(ll.isEmpty(), True)

#testing to see if i can remove anything from the list
    def testRemoveAny(self):
        ll = DSALinkedList()
        ll.insertLast("a")
        ll.insertLast("b")
        ll.insertLast("c")
        ll.insertLast("d")
        self.assertEqual(ll.checkFind("b"), True)
        self.assertEqual(ll.checkFind("d"), True)
        self.assertEqual(ll.removeAny("b"), "b")
        self.assertEqual(ll.checkFind("b"), False)
        self.assertEqual(ll.removeAny("d"), "d")
        self.assertEqual(ll.checkFind("d"), False)
   
#testing the peek methods
    def testPeek(self):
        ll = DSALinkedList()
        ll.insertFirst(1)
        ll.insertLast(2)
        self.assertEqual(ll.peekFirst(), 1)
        self.assertEqual(ll.peekLast(), 2)

#testing next   
    def testNext(self):
        ll = DSALinkedList()
        ll.insertFirst("a")
        ll.insertLast("b")
        ll.insertLast("c")
        ll.insertLast("d")
        self.assertEqual(ll.head.getNext().value, "b")
        self.assertEqual(ll.head.next.next.value, "c")
        self.assertEqual(ll.head.next.next.next.value, "d")
        currNd = ll.head
        while currNd.getNext() != None:
            currNd = currNd.getNext()
        self.assertEqual(currNd.value, "d")

#testing previous
    def testPrev(self):
        ll = DSALinkedList()
        ll.insertFirst("a")
        ll.insertLast("b")
        ll.insertLast("c")
        ll.insertLast("d")
        self.assertEqual(ll.tail.getPrev().value, "c")
        self.assertEqual(ll.tail.prev.prev.value, "b")
        self.assertEqual(ll.tail.prev.prev.prev.value, "a")
        currNd = ll.tail
        while currNd.getPrev() != None:
            currNd = currNd.getPrev()
        self.assertEqual(currNd.value, "a")
        
#testing that my iteration works
    def testIter(self):
        ll = DSALinkedList()
        print("...........\nList")
        print("-----------")
        for i in range(5):
            ll.insertLast(i+1)
            print(i+1)
        print("-----------")
        self.assertEqual(ll.peekFirst(), 1)
        self.assertEqual(ll.head.next.value, 2)
        self.assertEqual(ll.head.next.next.value, 3)
        self.assertEqual(ll.tail.prev.value, 4)
        self.assertEqual(ll.peekLast(), 5)

#testing that i can replace nodes
    def testReplace(self):
        ll = DSALinkedList()
        ll.insertLast("a")
        ll.insertLast("b")
        ll.insertLast("c")
        ll.insertLast("d")
        print("\ntest replace")
        for i in ll:
            print(i)
        ll.replaceNode("a", "e")
        print("replaced")
        for i in ll:
            print(i)

#testing that i can find nodes      
    def testFind(self):
        ll = DSALinkedList()
        ll.insertLast("a")
        ll.insertLast("b")
        ll.insertLast("c")
        ll.insertLast("d")
        self.assertEqual(ll.checkFind('d'), True)
        self.assertEqual(ll.checkFind('e'), False)

#testing all
    def testAll(self):
        ll = DSALinkedList()
        ll.insertFirst("dl")
        ll.insertFirst("as")
        ll.insertFirst("aa")
        self.assertEqual(ll.peekFirst(), "aa")
        self.assertEqual(ll.peekLast(), "dl")
        self.assertEqual(ll.getCount(), 3)
        self.assertEqual(ll.tail.value, "dl")
        ll.removeLast()
        self.assertEqual(ll.getCount(), 2)
        self.assertEqual(ll.peekLast(), "as")
        self.assertEqual(ll.tail.getValue(), "as")
        self.assertEqual(ll.removeFirst(), "aa")
        self.assertEqual(ll.getCount(), 1)
        ll.insertFirst("ad")
        ll.insertFirst("ac")
        self.assertEqual(ll.getCount(), 3)


        


if __name__ == "__main__":
    unittest.main()
