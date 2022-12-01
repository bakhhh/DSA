import unittest
from linkedLists import *

class TestDSALinkedList(unittest.TestCase):

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
        

    def testInsertRemoveFirst(self):
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

    def testInsertRemoveLast(self):
        ll = DSALinkedList()
        ll.insertLast("a")
        ll.insertLast("b")
        ll.insertLast("c")
        ll.insertLast("d")
        self.assertEqual(ll.removeLast(), "d")
        self.assertEqual(ll.removeLast(), "c")
        self.assertEqual(ll.removeLast(), "b")
        self.assertEqual(ll.removeLast(), "a")
        self.assertEqual(ll.isEmpty(), True)
        


    def testPeek(self):
        ll = DSALinkedList()
        ll.insertFirst(1)
        ll.insertLast(2)
        self.assertEqual(ll.peekFirst(), 1)
        self.assertEqual(ll.peekLast(), 2)
        
        
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
         
            
                





if __name__ == "__main__":
    unittest.main()
