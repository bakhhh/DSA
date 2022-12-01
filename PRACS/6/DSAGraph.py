from linkedLists import *  #Previously submitted for Practical 4 in COMP1002, Sem 2, 2022
import numpy as np
import unittest
from DSAQueue import * #Previously submitted for Practical 4 in COMP1002, Sem 2, 2022
from DSAStack import * #Previously submitted for Practical 3 in COMP1002, Sem 2, 2022

class DSAGraphNode:
    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.vertexList = DSALinkedList()
        self.visited = False

    
    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getEdge(self,label): 
        for e in self.vertexList:
            if e == label:
                return True 
        
    def addEdge(self,vertex):
        return self.vertexList.insertLast(vertex)
    
    def getAdjacent(self):
        value = ''
        for values in self.vertexList:
            value = value + values 
        return value

    def remove(self):
        return self.vertexList.removeLast()

    def __str__(self) -> str:
        return (f"{self.label}: {self.getAdjacent()}")
    
    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def getVisited(self):
        return self.visited


class DSAGraph():
    def __init__(self):
        self.vertices = DSALinkedList()
        self.stack =DSAStack()
        self.queue = DSAQueue()

    def firstVertex(self): #gets first vertex
        for vertex in self.vertices:
            return vertex.label

    def getVertex(self,label):
        val = ""
        for vertex in self.vertices:
            if vertex.getLabel() == label:
                val = vertex
            
        return val

    def removeVertex(self):
        while self.vertices.count != 0:
            self.vertices.removeLast()

    def addVertex(self,label, value):
        return self.vertices.insertLast(DSAGraphNode(label,value))

    def addEdge(self,label1,label2):
        for vertex in self.vertices:
            if vertex.label == label1 and not vertex.getEdge(label2):
                v1 = vertex
                v1.addEdge(label2)
            if vertex.label == label2 and not vertex.getEdge(label1):
                v2 = vertex
                v2.addEdge(label1)

    def getVertexCount(self):
        return self.vertices.getCount()

    def getEdgeCount(self):
        count = sum(item.vertexList.getCount() for item in self.vertices)
        return int(count/2)

    def Adjacent(self,label1,label2): 
        for vertex in self.vertices:
            if vertex.label == label1 and vertex.getEdge(label2):
                return True

    def displayAsList(self):
        for i in self.vertices:
            print(i)
        
    def printMatrix(self,matrix,count):
        for i in range(0, count):
            for j in range(0, count):
                print(matrix[i][j], end = " ")
            print("\n", end = "")


    def displayAsMatrix(self):
        count = self.vertices.count +1
        matrix = np.zeros([count,count], dtype=object)
        col = 1
        row = 0
        for index,vertex in enumerate(self.vertices,1):#vertices
            row = 0
            matrix[0][0] = ' '
            matrix[0][index] = vertex.getLabel()
            matrix[index][0] = vertex.getLabel()
            for index, ajacent in enumerate(self.vertices): #adjacent
                row +=1
                matrix[row][col] = 1 if self.Adjacent(vertex.getLabel(), ajacent.getLabel())== True else 0
            col +=1
        self.printMatrix(matrix,count)


    def DFS(self, node,visited =DSALinkedList()): # kinda working but different to psuedocode
        stack = DSAStack()
        stack.push(node)
        while not stack.isEmpty():
            if node not in visited:
                visited.insertLast(node)
                stack.push(node)
                for k in self.getVertex(node).getAdjacent():
                    self.DFS(k,visited)
            stack.pop()
        return visited
    


    def BFS(self,node): #kinda works
        T = DSAQueue()
        Q = DSAQueue()
        for vertex in self.vertices:
            vertex.clearVisited()
        string =''
        v = self.getVertex(node)
        v.setVisited()
        Q.enqueue(v)

        while not Q.isEmpty():
            v = Q.dequeue()
            vAdjacent = v.getAdjacent()
            for w in vAdjacent.split():
                w = self.getVertex(w)
                if v.visited == False:
                    w.setVisited()
                    Q.enqueue(w)
            string +=(" "+ v.getLabel())
        return print(string)

    
        

 
# # # #TESTING
class testGraph(unittest.TestCase):
    # def testaddedge(self):
    #     graph = DSAGraph()
    #     graph.addVertex("A","A")
    #     graph.addVertex("B", "B")
    #     graph.addVertex("C", "C")
    #     graph.addVertex("D", "D")
    #     graph.addEdge("A","B")
    #     graph.addEdge("A","C")
    #     graph.addEdge("D","C")
    #     graph.addEdge("C","B")
    #     graph.addEdge("B","C")
    #     # graph.BFS()
    #     graph.displayAsList()
    #     # graph.displayAsMatrix()

    # def testAddVertexandCount(self):
    #     graph = DSAGraph()
    #     graph.addVertex("A","A")
    #     graph.addVertex("B", "B")
    #     graph.addVertex("C", "C")
    #     graph.addVertex("D", "D")
    #     graph.addVertex("E","E")
    #     self.assertEqual(graph.findVertex("A"), "A")
    #     self.assertEqual(graph.findVertex("B"), "B")
    #     self.assertEqual(graph.findVertex("C"), "C")
    #     self.assertEqual(graph.findVertex("D"), "D")
    #     self.assertEqual(graph.findVertex("E"), "E")
    #     self.assertEqual(graph.getVertexCount(), 5)

    # def testAddEdgeandCount(self):
    #     graph = DSAGraph()
    #     graph.addVertex("A","A")
    #     graph.addVertex("B", "B")
    #     graph.addVertex("C", "C")
    #     graph.addVertex("D", "D")
    #     graph.addVertex("E","E")
    #     graph.addEdge("A","B")
    #     self.assertEqual(graph.getEdgeCount(), 1)
    #     graph.addEdge("C","A")
    #     self.assertEqual(graph.getEdgeCount(), 2)
    #     graph.addEdge("D","B")
    #     self.assertEqual(graph.getEdgeCount(), 3)
    #     graph.addEdge("B","A")
    #     self.assertEqual(graph.getEdgeCount(), 3)
    #     graph.addEdge("C","A")
    #     self.assertEqual(graph.getEdgeCount(), 3)
    #     graph.addEdge("D","A")
    #     self.assertEqual(graph.getEdgeCount(), 4)
    #     graph.addEdge("D","E")
    #     self.assertEqual(graph.getEdgeCount(), 5)

    # def testGetVertexandFind(self):
    #     graph = DSAGraph()
    #     graph.addVertex("A","A")
    #     graph.addVertex("B", "B")
    #     graph.addVertex("C", "C")
    #     self.assertEqual(graph.findVertex("A"), "A")
    #     self.assertEqual(graph.findVertex("B"), "B")
    #     self.assertEqual(graph.findVertex("C"), "C")
    #     self.assertEqual(graph.getVertex("A").label, "A")
    #     self.assertEqual(graph.getVertex("B").label, "B")
    #     self.assertEqual(graph.getVertex("C").label, "C")

    def testBFSandDFS(self):
        g = DSAGraph()
        g.addVertex("A","A")
        g.addVertex("B", "B")
        g.addVertex("C", "C")
        g.addVertex("D", "D")
        g.addVertex("E", "E")
        g.addVertex("F", "F")
        g.addVertex("G", "G")
        g.addVertex("H", "H")
        g.addVertex("I", "I")
        g.addVertex("J", "J")
        g.addEdge('A', 'B')
        g.addEdge('A', 'C')
        g.addEdge('A', 'D')
        g.addEdge('B', 'A')
        g.addEdge('B', 'E')
        g.addEdge('C', 'A')
        g.addEdge('C', 'F')
        g.addEdge('D', 'A')
        g.addEdge('D', 'E')
        g.addEdge('D', 'F')
        g.addEdge('D', 'H')
        g.addEdge('E', 'B')
        g.addEdge('E', 'D')
        g.addEdge('E', 'G')
        g.addEdge('F', 'C')
        g.addEdge('F', 'D')
        g.addEdge('F', 'I')
        g.addEdge('G', 'E')
        g.addEdge('G', 'H')
        g.addEdge('G', 'J')
        g.addEdge('H', 'D')
        g.addEdge('H', 'G')
        g.addEdge('H', 'I')
        g.addEdge('H', 'J')
        g.addEdge('I', 'F')
        g.addEdge('I', 'H')
        g.addEdge('I', 'J')
        g.addEdge('J', 'G')
        g.addEdge('J', 'H')
        g.addEdge('J', 'I') 
        g.test()
        # print("\nPringting BFS..")  
        # g.BFS("A")
        # g.DepthFirst("A")
    #     print("\nPrinting DFS..")  
    #     for i in g.DFS("A"):
    #         print(i, end ='')
    #     print("")

    # def testDisplayListandMatrix(self):
    #     g = DSAGraph()
    #     g.addVertex("A","A")
    #     g.addVertex("B", "B")
    #     g.addVertex("C", "C")
    #     g.addVertex("D", "D")
    #     g.addVertex("E", "E")
    #     g.addVertex("F", "F")
    #     g.addVertex("G", "G")
    #     g.addVertex("H", "H")
    #     g.addVertex("I", "I")
    #     g.addVertex("J", "J")
    #     g.addEdge('A', 'B')
    #     g.addEdge('A', 'C')
    #     g.addEdge('A', 'D')
    #     g.addEdge('B', 'A')
    #     g.addEdge('B', 'E')
    #     g.addEdge('C', 'A')
    #     g.addEdge('C', 'F')
    #     g.addEdge('D', 'A')
    #     g.addEdge('D', 'E')
    #     g.addEdge('D', 'F')
    #     g.addEdge('D', 'H')
    #     g.addEdge('E', 'B')
    #     g.addEdge('E', 'D')
    #     g.addEdge('E', 'G')
    #     g.addEdge('F', 'C')
    #     g.addEdge('F', 'D')
    #     g.addEdge('F', 'I')
    #     g.addEdge('G', 'E')
    #     g.addEdge('G', 'H')
    #     g.addEdge('G', 'J')
    #     g.addEdge('H', 'D')
    #     g.addEdge('H', 'G')
    #     g.addEdge('H', 'I')
    #     g.addEdge('H', 'J')
    #     g.addEdge('I', 'F')
    #     g.addEdge('I', 'H')
    #     g.addEdge('I', 'J')
    #     g.addEdge('J', 'G')
    #     g.addEdge('J', 'H')
    #     g.addEdge('J', 'I') 
    #     print('\nDisplaying list..\n')
    #     g.displayAsList()
    #     print('\nDisplaying Matrix..\n')
    #     g.displayAsMatrix()
        
 
if __name__ == "__main__":
    unittest.main()

