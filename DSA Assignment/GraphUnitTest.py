#File: #GraphUnitTest.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 3/4/22
#Data Structures & Algorithms Assignment
#Previously submitted for Practical 6 in COMP1002, Sem 2, 2022
import unittest
from DSAGraph import * 
 
# # # #TESTING GRAPH
class testDSAGraph(unittest.TestCase):
#testing adding vertex    
    def testAddVertex(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addVertex("D", "D")
        self.assertEqual(graph.getVertex("A").label,"A")
        self.assertEqual(graph.getVertex("B").label,"B")
        self.assertEqual(graph.getVertex("C").label,"C")
        self.assertEqual(graph.getVertex("D").label,"D")
#testing if i can add edges
    def testAddEdge(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addVertex("D", "D")
        graph.addEdge('A','B',1,True)
        graph.addEdge('A','C',1,True)
        graph.addEdge('A','D',1,True)
        graph.addEdge('B','A',1,True)
        self.assertEqual(graph.checkEdge("AB"),True)
        self.assertEqual(graph.findEdge("A","B"),True)
        self.assertEqual(graph.checkEdge("AC"),True)
        self.assertEqual(graph.findEdge("A","C"),True)
        self.assertEqual(graph.checkEdge("AD"),True)
        self.assertEqual(graph.findEdge("A","D"),True)
        self.assertEqual(graph.checkEdge("BA"),True)
        self.assertEqual(graph.findEdge("B","A"),True)

#testing if i can get direction     
    def testGetDirection(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addEdge("A","B",1, False)
        graph.addEdge("B","C",1, True)
        print('')
        graph.findDirection("AB")
        self.assertAlmostEqual(graph.checkDirection("AB"),False)
        self.assertAlmostEqual(graph.checkDirection("BC"),True)

#testing if i can find vertex
    def testFindNode(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addVertex("D", "D")
        graph.addVertex("E","E")
        self.assertEqual(graph.findNode("A"), True)
        self.assertEqual(graph.findNode("B"), True)
        self.assertEqual(graph.findNode("C"),True)
        self.assertEqual(graph.findNode("D"), True)
        self.assertEqual(graph.findNode("E"), True)

#testing if i can remove vertex
    def testRemoveVertex(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.removeVertex("A")
        graph.removeVertex("B")
        self.assertEqual(graph.checkIfVertexRemoved("A"),True) #not in graph anymore
        self.assertEqual(graph.checkIfVertexRemoved("B"),True) #not in graph anymore
        self.assertEqual(graph.checkIfVertexRemoved("C"),False) #still in graph 
        
#testing if i can remove edge
    def testRemoveEdge(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addEdge("A","B",1, False)
        graph.addEdge("B","C",1, False)
        graph.removeEdge("A","B")
        self.assertEqual(graph.checkIfEdgeRemoved("AB"),True) # edge is not in the graph
        self.assertEqual(graph.checkIfEdgeRemoved("BC"),False)#still an edge

#testing if i can get weight        
    def testGetWeight(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addEdge("A","B",4, False)
        graph.addEdge("B","C",3, False)
        self.assertEqual(graph.getLabelWeight("AB"),4)
        self.assertEqual(graph.getLabelWeight("BC"),3)

#testing the edge count
    def testEdgeCount(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addVertex("D", "D")
        graph.addVertex("E", "E")
        graph.addVertex("F", "F")
        graph.addVertex("G", "G")
        graph.addEdge("A","B",1, False) #false = undirected
        graph.addEdge("B","C",1, False)
        graph.addEdge("D","E",1, False)
        graph.addEdge("E","F",1, False)
        graph.addEdge("A","D",1, False)
        graph.addEdge("B","E",1, False)
        graph.addEdge("C","F",1, False)
        graph.addEdge("D","G",1, False)
        #edge count
        self.assertEqual(graph.getEdgeCount(), 8)

#testing the vertex count     
    def testVertexCount(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addVertex("D", "D")
        graph.addVertex("E", "E")
        graph.addVertex("F", "F")
        graph.addVertex("G", "G")
        self.assertEqual(graph.getVertexCount(), 7)

#testing breadthfirstsearch
    def testBFS(self):
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
        g.addEdge('A', 'B',1,True)
        g.addEdge('A', 'C',1,True)
        g.addEdge('A', 'D',1,True)
        g.addEdge('B', 'A',1,True)
        g.addEdge('B', 'E',1,True)
        g.addEdge('C', 'A',1,True)
        g.addEdge('C', 'F',1,True)
        g.addEdge('D', 'A',1,True)
        g.addEdge('D', 'E',1,True)
        g.addEdge('D', 'F',1,True)
        g.addEdge('D', 'H',1,True)
        g.addEdge('E', 'B',1,True)
        g.addEdge('E', 'D',1,True)
        g.addEdge('E', 'G',1,True)
        g.addEdge('F', 'C',1,True)
        g.addEdge('F', 'D',1,True)
        g.addEdge('F', 'I',1,True)
        g.addEdge('G', 'E',1,True)
        g.addEdge('G', 'H',1,True)
        g.addEdge('G', 'J',1,True)
        g.addEdge('H', 'D',1,True)
        g.addEdge('H', 'G',1,True)
        g.addEdge('H', 'I',1,True)
        g.addEdge('H', 'J',1,True)
        g.addEdge('I', 'F',1,True)
        g.addEdge('I', 'H',1,True)
        g.addEdge('I', 'J',1,True)
        g.addEdge('J', 'G',1,True)
        g.addEdge('J', 'H',1,True)
        g.addEdge('J', 'I',1,True)
        for i in g.BreadthFirstSearch("A"):
            print(i, end='')
        print('')

          
#testing depthfirstsearch
    def testDFS(self):
        g = DSAGraph()
        v = DSALinkedList()
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
        g.addEdge('A', 'B',1,True)
        g.addEdge('A', 'C',1,True)
        g.addEdge('A', 'D',1,True)
        g.addEdge('B', 'A',1,True)
        g.addEdge('B', 'E',1,True)
        g.addEdge('C', 'A',1,True)
        g.addEdge('C', 'F',1,True)
        g.addEdge('D', 'A',1,True)
        g.addEdge('D', 'E',1,True)
        g.addEdge('D', 'F',1,True)
        g.addEdge('D', 'H',1,True)
        g.addEdge('E', 'B',1,True)
        g.addEdge('E', 'D',1,True)
        g.addEdge('E', 'G',1,True)
        g.addEdge('F', 'C',1,True)
        g.addEdge('F', 'D',1,True)
        g.addEdge('F', 'I',1,True)
        g.addEdge('G', 'E',1,True)
        g.addEdge('G', 'H',1,True)
        g.addEdge('G', 'J',1,True)
        g.addEdge('H', 'D',1,True)
        g.addEdge('H', 'G',1,True)
        g.addEdge('H', 'I',1,True)
        g.addEdge('H', 'J',1,True)
        g.addEdge('I', 'F',1,True)
        g.addEdge('I', 'H',1,True)
        g.addEdge('I', 'J',1,True)
        g.addEdge('J', 'G',1,True)
        g.addEdge('J', 'H',1,True)
        g.addEdge('J', 'I',1,True)     
        for i in g.DepthFirstSearch("A"):
            print(i, end='')
        print('')

        

#testing display adjacency list and matrix
    def testDisplayListandMatrix(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addVertex("D", "D")
        graph.addVertex("E", "E")
        graph.addEdge("A","B",1, False)
        graph.addEdge("B","C",1, False)
        graph.addEdge("D","E",1, False)
        print('\nDisplaying list..\n')
        graph.displayAsList()
        print('\nDisplaying Matrix..\n')
        graph.displayAsMatrix()

#testing if i can update my vertex
    def testUpdateVertex(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addVertex("D", "D")
        graph.addVertex("E", "E")
        graph.addEdge("A","B",1, False)
        graph.addEdge("B","C",1, True)
        graph.addEdge("D","E",1, True)
        graph.updateVertex("A", "B")
        print('')
        graph.displayAsList()
#testing if i can update edge
    def testUpdateEdge(self):
        graph = DSAGraph()
        graph.addVertex("A","A")
        graph.addVertex("B", "B")
        graph.addVertex("C", "C")
        graph.addVertex("D", "D")
        graph.addVertex("E", "E")
        graph.addEdge("A","B",1, False)
        graph.addEdge("B","C",1, True)
        graph.addEdge("D","E",1, True)
        graph.updateEdge('BC','A','D')
        self.assertEqual(graph.findEdge("A","D"),True)
        graph.updateWeight('A','B',4)
        graph.updateWeight('A','D',3)
        graph.updateDirection('A','B')
        print('')
        for i in graph.edges:
            print(f"{i.label}: {i.weight}: {i.directed}")

#testing shortest path
    def testShortestPath(self):
        g = DSAGraph()
        g.addVertex("A","A")
        g.addVertex("B", "B")
        g.addVertex("C", "C")
        g.addVertex("D", "D")
        g.addVertex("E", "E")
        g.addVertex("F", "F")
        g.addEdge('A', 'B',1,True)
        g.addEdge('A', 'C',1,True)
        g.addEdge('A', 'D',1,True)
        g.addEdge('B', 'A',1,True)
        g.addEdge('B', 'E',1,True)
        g.addEdge('C', 'A',1,True)
        g.addEdge('C', 'F',1,True)
        print("\nShortest Path = ",g.shortestPath("A","F"))
#testing dfs path from start to dest
    def testPath(self):
        g = DSAGraph()
        g.addVertex("A","A")
        g.addVertex("B", "B")
        g.addVertex("C", "C")
        g.addVertex("D", "D")
        g.addVertex("E", "E")
        g.addVertex("F", "F")
        g.addEdge('A', 'B',1,True)
        g.addEdge('A', 'C',1,True)
        g.addEdge('A', 'D',1,True)
        g.addEdge('B', 'A',1,True)
        g.addEdge('B', 'E',1,True)
        g.addEdge('C', 'A',1,True)
        g.addEdge('C', 'F',1,True)
        print("\nPath = ",g.path("A","F"))
#testing bfs path from start to dest
    def testBFSPath(self):
        g = DSAGraph()
        g.addVertex("A","A")
        g.addVertex("B", "B")
        g.addVertex("C", "C")
        g.addVertex("D", "D")
        g.addVertex("E", "E")
        g.addVertex("F", "F")
        g.addEdge('A', 'B',1,True)
        g.addEdge('A', 'C',1,True)
        g.addEdge('A', 'D',1,True)
        g.addEdge('B', 'A',1,True)
        g.addEdge('B', 'E',1,True)
        g.addEdge('C', 'A',1,True)
        g.addEdge('C', 'F',1,True)
        print("\nBFS Path = ",g.BFSPath("A","F"))



        




 
if __name__ == "__main__":
    unittest.main()
