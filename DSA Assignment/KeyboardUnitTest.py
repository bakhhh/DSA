#File: #KeyboardUnitTest.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 9/4/22
#Data Structures & Algorithms Assignment
import unittest
from Keyboard import *
import numpy as np
from myException import *
#testing all keyboard functions that are used in the menu
class testKeyboard(unittest.TestCase):
#testing the length of the columns in each file 

    def testlengthOfCol(self):
        k = keyboard()
        self.assertEqual(k.lengthOfCol('keyboard.txt'),6)
        self.assertEqual(k.lengthOfCol('keyboard2.txt'),11)
        self.assertEqual(k.lengthOfCol('keyboard3.txt'),11)
        self.assertRaises(FileNotFoundError,k.lengthOfCol,"none.txt") #test with invalid file

#testing the length of the rows in each file 
    def testlengthOfRow(self):
        k = keyboard()
        self.assertEqual(k.lengthOfRow('keyboard.txt'),6)
        self.assertEqual(k.lengthOfRow('keyboard2.txt'),4)
        self.assertEqual(k.lengthOfRow('keyboard3.txt'),4) 
        self.assertRaises(FileNotFoundError,k.lengthOfRow,"none.txt") #test with invalid file
        
#testing if i can read in the keyboards
    def testReadKeyboard(self):
        k = keyboard()
     
        try:
            k.readKeyboard("keyboard.txt")
            raised = False
        except:
            raised = True
        self.assertFalse(raised)
        self.assertEqual(raised,False,msg='no exception raised')

        try:
            k.readKeyboard("keyboard2.txt")
            raised = False
        except:
            raised = True
        self.assertFalse(raised)
        self.assertEqual(raised,False,msg='no exception raised')

        try:
            k.readKeyboard("keyboard3.txt")
            raised = False
        except:
            raised = True
        self.assertFalse(raised)
        self.assertEqual(raised,False,msg='no exception raised')

#testing if i can insert different keyboards in graph
    def testInsertIntoGraph(self):
        k = keyboard()
     
        try:
            k.insertIntoGraph("keyboard.txt")
            raised = False
        except:
            raised = True
        self.assertFalse(raised)
        self.assertEqual(raised,False,msg='no exception raised')

        try:
            k.insertIntoGraph("keyboard2.txt")
            raised = False
        except:
            raised = True
        self.assertFalse(raised)
        self.assertEqual(raised,False,msg='no exception raised')

        try:
            k.insertIntoGraph("keyboard3.txt")
            raised = False
        except:
            raised = True
        self.assertFalse(raised)
        self.assertEqual(raised,False,msg='no exception raised')

#testing if i can delete vertex
    def testDeleteVertex(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        k.deleteVertex('a')
        self.assertEqual(k.graph.checkIfVertexRemoved("a"),True) #true mean vertex is removed
        k.deleteVertex('b')
        self.assertEqual(k.graph.checkIfVertexRemoved("b"),True) #true mean vertex is removed

#testing if i insert vertex
    def testInsertVertex(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        self.assertEqual(k.findVertex('/'),False) #False means it cant be found
        self.assertEqual(k.findVertex('?'),False) #False means it cant be found
        self.assertEqual(k.findVertex('!'),False) #False means it cant be found
        self.assertEqual(k.findVertex('.'),False) #False means it cant be found
        k.insertVertex("/")
        self.assertEqual(k.findVertex('/'),True) #True means it is found
        k.insertVertex("?")
        k.insertVertex("!")
        k.insertVertex(".")
        self.assertEqual(k.findVertex('?'),True) #True means it is found
        self.assertEqual(k.findVertex('!'),True) #True means it is found
        self.assertEqual(k.findVertex('.'),True) #True means it is found

#testing if i can find vertex
    def testFindVertex(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        self.assertEqual(k.findVertex('a'),True)
        self.assertEqual(k.findVertex('b'),True)
        self.assertEqual(k.findVertex('c'),True)
        self.assertEqual(k.findVertex('d'),True)
        self.assertEqual(k.findVertex('/'),False)
        self.assertEqual(k.findVertex('?'),False)

#testing if i can update a vertex
    def testUpdateVertex(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        self.assertEqual(k.findVertex('/'),False) #False means it cant be found
        self.assertEqual(k.findVertex('a'),True) 
        k.updateVertex("a","/") #swaps 'a' with '/' 
        self.assertEqual(k.graph.foundVertex('/'),True) #False means it cant be found
        self.assertEqual(k.graph.foundVertex('a'),False) 


#testing if i can find edges
    def testFindEdge(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        self.assertEqual(k.findEdge("a","b"),True)
        self.assertEqual(k.findEdge("a","g"),True)
        self.assertEqual(k.findEdge("b","c"),True)
        self.assertEqual(k.findEdge("c","d"),True)
        self.assertEqual(k.findEdge("d","e"),True)

#testing if i can delete edges
    def testDeleteEdge(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        self.assertEqual(k.findEdge('a','b'),True)
        k.deleteEdge('a','b')
        self.assertEqual(k.findEdge('a','b'),False)
        
#testing if i can insert a new edge
    def testInsertEdge(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        self.assertEqual(k.findEdge("a","t"),False)
        k.insertEdge("a","t",1,False)
        self.assertEqual(k.findEdge("a","t"),True)
        self.assertEqual(k.findEdge("b","m"),False)
        k.insertEdge("b","m",1,False)
        self.assertEqual(k.findEdge("b","m"),True)

#testing if i can update edge
    def testUpdateEdge(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        self.assertEqual(k.findEdge("a","f"),False)
        self.assertEqual(k.findEdge("a","b"),True)
        k.updateEdge('ab','a','f')
        self.assertEqual(k.findEdge("a","f"),True)
        self.assertEqual(k.findEdge("a","b"),False)
        self.assertEqual(k.graph.getLabelWeight("af"),1)
        k.updateWeight('a','f',3)
        self.assertEqual(k.graph.getLabelWeight("af"),3)
        k.updateDirection('a','g') 
        for i in k.graph.edges:
            print(f"{i.label}: {i.weight}: {i.directed}")

#testing if i can get all paths
    def testGetPath(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        try:
            k.getPath("none.txt")
        except Exception as e:
            print(e)
        try:
            k.getPath("stringfile.txt")
        except Exception as e:
            print(e)
        path =k.displayInOrder()
        for line in path:
            print( "%s\n" % line)

#testing the shortest path algorithm
    def testShortestPath(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        k.findShortestPath('sohail')
        k.findShortestPath('bakhshi')

#testing if it sorts properly
    def testSortPaths(self):
        k = keyboard()       
        with open('stringfile.txt','r') as file:
            content =file.read().split()
            array = np.array(content)
            print("\nsorted strings\n",k.selectionSort(array)) #testing on string file 

#testing if it displays paths in order
    def testDisplayinOrder(self):
        k = keyboard()
        print(k.displayInOrder()) 

#testing if it saved keyboard as serialised file
    def testSave(self):
        k = keyboard()
        k.insertIntoGraph("keyboard.txt")
        k.updateEdge('ab','a','f')
        k.updateVertex("a","/") #swaps 'a' with '/' 
        k.saveKeyboard('serialisedKeyboard.txt')

#testing if loaded up the serialised file    
    def testUnpickle(self):
        k = keyboard()
        k.unpickleFile('serialisedKeyboard.txt')
        self.assertEqual(k.findEdge('a','f'),True)
        self.assertEqual(k.findVertex('/'),True)





if __name__ == "__main__":
    unittest.main()

