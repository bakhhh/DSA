#File: DSAGraph.py
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 28/9/22
#Previously submitted for Practical 6 in COMP1002, Sem 2, 2022
#
from DSALinkedLists import *  #Previously submitted for Practical 4 in COMP1002, Sem 2, 2022
import numpy as np
from DSAQueue import * #Modified DSAQueue Previously submitted for Practical 4 in COMP1002, Sem 2, 2022
from DSAStack import * #Previously submitted for Practical 3 in COMP1002, Sem 2, 2022
from myException import * #custom exceptions


#Graph Edge class 
#additional edge class added 
class DSAGraphEdge:
    def __init__(self,isfrom,to,label,weight, directed):
        self.fromVertex = isfrom # from vertex
        self.toVertex = to # the vertex which it is connected to 
        self.label = label #edge label
        self.weight =weight # the weight of the edge
        self.directed = directed #set edge to either directed or undirected via boolean 

#Method: getLabel
#Returns the edge label as a whole eg AB
    def getLabel(self): 
        return self.label

#Method: setLabel
#Sets the edge label    
    def setLabel(self,label):
        self.label = label

#Method: getWeight
#Returns the edge weight    
    def getWeight(self): 
        return self.weight

#Method: setWeight
#Sets the edge weight   
    def setWeight(self,weight):
        self.label = weight

#Method: getFrom
#Returns the vertex which it is from  
#gets the from vertex eg A from AB
    def getFrom(self): 
        return self.fromVertex

#Method: setFrom
#Sets the vertex which it is from  
    def setFrom(self,label):
        self.fromVertex= label

#Method: getTo
#Returns the vertex which it is connected to 
#gets the to vertex eg B from AB 
    def getTo(self): 
        return self.toVertex

#Method: setTo
#Sets the vertex which it is connected to 
    def setTo(self,label):
        self.toVertex= label

#Method: getDirected
#Returns the direction of the edge
    def getDirected(self): #returns if directed via boolean
        return self.directed

#Method: setDirected
#Sets the direction of the edge as directed
    def setDirected(self):
        self.directed= True

#Method: setUnDirected
#Sets the direction of the edge as undirected
    def setUnDirected(self):
        self.directed= False

#Method: __str__
#Returns the label as string
    def __str__(self) -> str: # makes it so i dont have to constantly write '.label' when reffering to an edge
        return (f"{self.label}")
        

    
#Node class also known as vertex
class DSAGraphNode:
    def __init__(self, label, value):
        self.label = label # vertex label
        self.value = value # vertex value
        self.edgeList = DSALinkedList() # changed to edgeList from vertexList
        self.visited = False #visited set to false
    
#Method: getLabel
#Returns the vertex label    
    def getLabel(self): #returns vertex label
        return self.label

#Method: setLabel
#sets the vertex label 
    def setLabel(self,label):
        self.label=label

#Method: getValue
#Returns the vertex value 
    def getValue(self): #returns vertex value 
        return self.value

#Method: isEdge
#Checks if label is edge
    def isEdge(self,label):  # function checks if the label inputted is an edge or not
        for e in self.edgeList:
            if e.getTo() == label:
                return True  #returns true if found 
 
#Method: addEdge
#Adds an edge into the graph edge class
    def addEdge(self,label1,label2,weight, directed): #function for adding edge
        self.edgeList.insertLast(DSAGraphEdge(label1, label2, (label1+label2),weight, directed)) #inserting DSAgraphedge class into the edgeList so i can refer to it later on
    
#Method: getAdjacent
#Returns adjacent vertices 
    def getAdjacent(self): #function for getting the adjacent vertices
        adjacentVal = ""
        for edges in self.edgeList:
            adjacentVal = adjacentVal + edges.getTo()

        return adjacentVal #returns a string containing adjacent values

#Method: removeLast
#Removes last edge
    def removeLast(self): # removes last edge  from edge list
        self.edgeList.removeLast()

#Method: removeEdge
#Removes edges 
    def removeEdge(self,label1,label2): #removes selected edge from list
        for edge in self.edgeList:
            if label1 == edge.fromVertex and label2 ==edge.toVertex:
                self.edgeList.removeAny(edge)

#Method: setVisited
#Sets self.visited to true if visited         
    def setVisited(self): 
        self.visited = True

#Method: clearVisited
#Sets self.visited to False        
    def clearVisited(self): 
        self.visited = False

#Method: getVisited
#Returns self.visited         
    def getVisited(self): # check whether vertex is visited or not
        return self.visited 

    def __str__(self) -> str: #return label
        return (f"{self.label}")

#Graph class
class DSAGraph():
    def __init__(self):
        self.vertices = DSALinkedList() #linked list with vertices
        self.edges = DSALinkedList() #linked list with edges

#Method: addVertex
#Adds vertex into DSAGraphNode class    
    def addVertex(self,label, value): #function for adding vertex
        self.vertices.insertLast(DSAGraphNode(label,value)) #inserting into vertices linked list

#Method: getVertex
#Returns the vertex in a string
    def getVertex(self,label): # function that finds the vertex within the vertices linked list
        try:
            vertexVal = ""
            for vertex in self.vertices:
                if vertex.getLabel() == label:
                    vertexVal = vertex
                   
            return vertexVal #returns a string contain the the vertex
        except myException as e: #catch any errors
            print("Error: ",e)

#Method: findNode
#Finds Vertex returns bool
    def findNode(self,label): # function that finds the vertex within the vertices linked list but returns a boolean #kinda giving me problems which is why i have a few other functions similar to this
        labelValue = False
        try:
            for vertex in self.vertices:
                if vertex.getLabel() == label:
                    labelValue= True
            if labelValue== False:
                raise NotFoundError(f"Vertex {label} not found")  #if vertex not found
            return labelValue 
        except NotFoundError as e: #catch any errors
            print(e)

#Method: checkIfVertexRemoved
#Checks if vertex is removed
    def checkIfVertexRemoved(self,label):  #if label is removed returns true
            labelValue = True
            for vertex in self.vertices:
                if vertex.getLabel() == label:
                    labelValue= False  
            return labelValue 

#Method: returnVertex
#Checks if vertex is in the graph
    def foundVertex(self,label):  #if label is found returns true
            labelValue = False
            for vertex in self.vertices:
                if vertex.getLabel() == label:
                    labelValue= True  
            return labelValue 
           
#Method: removeAll
#Removes all vertices 
    def removeAll(self): #removes all vertices # used it in my prac but still left it in here
        while self.vertices.count != 0:
            self.vertices.removeLast()

#Method: removeVertex
#Removes vertex of choice
    def removeVertex(self,label): #function that removes a vertex of choice
        vertex = self.getVertex(label) # finds the vertex in the vertices list 
        self.vertices.removeAny(vertex) #removes that vertex

#Method: updateVertex
#Updates old vertex to a new vertex
    def updateVertex(self,old,new):
        for vertex in self.vertices:
            if vertex.label == old:
                vertex.setLabel(new)
            
#Method: addEdge
#Adds edge into edge class
    def addEdge(self,label1,label2,weight,directed):  # function to add edges
        try:
            if self.findEdge(label1,label2) ==True: #check if edge is already in the graph
                    raise AlreadyEdge(f"{(label1+label2)} is already an edge ") #prevents adding duplicate edges
            elif self.findEdge(label1,label2) ==False: # if not already an edge then add the edge 
                for vertex in self.vertices:
                    if directed == False:  #checks whether the edge is directed or not #if undirected then it will add the edge twice with the labels flipped
                        if vertex.label == label1:
                            vertex.addEdge(label1,label2,weight,directed)
                            self.edges.insertLast(DSAGraphEdge(label1, label2,(label1+label2),weight,directed))
                        if vertex.label == label2:
                            vertex.addEdge(label2,label1,weight,directed)
                            self.edges.insertLast(DSAGraphEdge(label2, label1,(label2+label1),weight,directed)) 
                    elif directed == True:
                        if vertex.label == label1:
                            vertex.addEdge(label1,label2,weight,directed)
                            self.edges.insertLast(DSAGraphEdge(label1, label2,(label1+label2),weight,directed))

        except AlreadyEdge as e: #catches errors
            print("Error: ", e)

#Method: findEdge
#Finds edge of choice             
    def findEdge(self,label1, label2): #finds the edge in the graph and returns boolean #used to prevent duplicate edges
        edgeValue = False
        for e in self.edges:
            if label1 == e.getFrom() and label2 == e.getTo():
                edgeValue =True
        return edgeValue

#Method: checkEdge
#Checks if edge is in the graph
    def checkEdge(self,label): 
        edgeValue = False
        try:
            for e in self.edges:
                if label == e.label:
                    edgeValue =True
            if edgeValue == False:
                raise NotFoundError(f"\nEdge {label} not found") 
            return edgeValue #returns a boolean
        except NotFoundError as e:
            print(e)

#Method: checkIfEdgeRemoved
#Checks if edge is removed from the graph
    def checkIfEdgeRemoved(self,label):  #if edge is removed return true
        edgeValue = True
        for e in self.edges:
            if label == e.label:
                edgeValue =False
        return edgeValue #returns a boolean
    
#Method: getEdge
#Gets edge and returns it as a string      
    def getEdge(self,label1, label2): 
        try:
            val = ""
            for edge in self.edges:
                if label1 == edge.fromVertex and label2 ==edge.toVertex:
                    val = edge
               
            return val
        except myException as e:
            print("error", e)

#Method: updateEdge
#Updates edge to another edge
    def updateEdge(self,edge,new1,new2):
        for edges in self.edges:
            if edges.label == edge:
                edges.setLabel(new1+new2)
                edges.setFrom(new1)
                edges.setTo(new2)
        for v in self.vertices:
            for edges in v.edgeList:
                if edges.label == edge:
                    edges.setLabel(new1+new2)
                    edges.setFrom(new1)
                    edges.setTo(new2)
    
#Method: updateWeight
#Allows to update the weight of the edge
    def updateWeight(self,v1,v2,weight):
        for edges in self.edges:
            if edges.label == v1+v2:
                edges.weight =(int(weight))
            if edges.label == v2+v1:
                edges.weight =(int(weight))
        for v in self.vertices:
            for edges in v.edgeList:
                if edges.label == v1+v2:
                    edges.weight =(int(weight))
                if edges.label == v2+v1:
                    edges.weight =(int(weight))

#Method: updateDirection
#Allows to update the direction of the edge
    def updateDirection(self,v1,v2):
        w =self.getLabelWeight(str(v1)+str(v2))
        choseDirection = input("\nSet Direction to directed [1]\nSet Direction to undirected[2]\nPlease Select an option: ")
        if choseDirection == '1':
            for edges in self.edges:
                if edges.label == v1+v2:
                    if edges.getDirected() == True:
                        print("Edge already directed")
                    else:
                        self.removeEdge(v1,v2)  #easiest way for me was to remove the edge and re add it as directed/unfirected
                        self.addEdge(v1,v2,w,True)

        elif choseDirection == '2':
            for edges in self.edges:
                if edges.label == v1+v2:
                    if edges.getDirected() == False:
                        print("Edge already undirected")
                    else:
                        self.removeEdge(v1,v2)
                        self.addEdge(v1,v2,w,False)

#Method: directed
#Finds the direction of the edge
    def directed(self,label1,label2): #finds the direction of the edge
        e = self.getEdge(label1,label2)
        for edge in self.edges:
            if edge ==e :
                return edge.getDirected()

#Method: removeEdge
#Removes selected edge from graph
    def removeEdge(self,label1, label2): #function that removes edge
        if self.checkEdge(label1+label2) == True: #if edge exists then we can delete
            if self.directed(label1,label2)== False:
                edge1 = self.getEdge(label1,label2) #finds the edge
                edge2 = self.getEdge(label2,label1)
                self.edges.removeAny(edge1) #removes edge
                self.edges.removeAny(edge2)
                for i in self.vertices:
                    i.removeEdge(label1,label2)
                    i.removeEdge(label2,label1)
                # print(f"\nEdge {label1+label2} removed")
            else:
                edge1 = self.getEdge(label1,label2) 
                self.edges.removeAny(edge1)
                for i in self.vertices:
                    i.removeEdge(label1,label2)
                # print(f"\nEdge {label1+label2} removed")
       
#Method: getVertexCount
#Returns the amount of vertices in the graph       
    def getVertexCount(self): 
        return self.vertices.getCount()

#Method: getEdgesCount
#Returns the amount of Edges in the graph       
    def getEdgeCount(self):
        value =0
        for i in self.edges:
            if self.checkDirection(str(i))==True:
                value +=1
            elif self.checkDirection(str(i))==False:
                value +=1/2
        return int(value)
    
#Method: isAdjacent
#Returns True if a vertex is adjacent to another vertex    
    def isAdjacent(self,label,label2):  
        isAdjacent = False
        for v in self.vertices:
            if v.label == label and v.isEdge(label2):
                isAdjacent= True
        return isAdjacent #returns boolean

#Method: displayAsList
#Displays adjacency list
    def displayAsList(self): 
        for v in self.vertices:
            print(f"{v.label}:", end = ' ')
            for e in v.edgeList:
                print( f"{e.getTo()}", end = '')
            print('')

#Method: printMatrix
#Prints the matrix      
    def printMatrix(self,matrix,count): 
        for i in range(0, count):
            for j in range(0, count):
                print(matrix[i][j], end = " ")
            print("\n", end = "")

#Method: displayAsMatrix
#Displays Matrix
    def displayAsMatrix(self): 
        count = self.vertices.count +1 
        matrix = np.zeros([count,count], dtype=object) #array of size count+1
        row = 0
        col = 1
        for i,vertex in enumerate(self.vertices,1):#this will display the vertices on the outside layer of the matrix
            row = 0
            matrix[0][0] = ' '
            matrix[0][i] = vertex.getLabel() #putting the labels on the edges
            matrix[i][0] = vertex.getLabel()
            for i, edge in enumerate(self.vertices): #this checks the adjacent vertices 
                row +=1 #goes through the rows
                if self.isAdjacent(vertex.getLabel(), edge.getLabel())== True:
                    matrix[col][row] =1 # if adjacent then that position is now 1
                
            col +=1 #goes through the columns
        self.printMatrix(matrix,count)

#Method: getLabelWeight
#Returns the label weights
    def getLabelWeight(self,label):
        weightValue = None
        for edges in self.edges:
            if edges.label == label:
                weightValue = edges.weight

        return weightValue

#Method: findAdjacentEdge
#Finds the adjacent edge 
    def findAdjacentEdge(self,node): 
        adjacentEdge =''
        for edges in self.edges: 
            if edges.fromVertex == node: 
                adjacentEdge = adjacentEdge +edges.toVertex

        return adjacentEdge

    
#Method: findMinEdge
#Returns edge with lowest weight
#not used
    def findMinEdge(self,node,label1,label2): #function so that i could chose the shortest path based on weights #didnt use
        minEdge =''
        for edges in self.edges: 
            if edges.fromVertex == node and self.getLabelWeight(str(node+label1)) <=self.getLabelWeight(str(node+label2)): 
                minEdge= edges.toVertex
      
        return minEdge

    
#Method: checkDirection
#Returns the direction of an edge
    def checkDirection(self,label): 
        for edges in self.edges:
            if edges.label ==label:
                return edges.getDirected()

#Method: findDirection
# Prints out the direction of the edge  
    def findDirection(self,label): 
        if self.checkDirection(label)== True:
            print(f"edge {label} is directed")
        elif self.checkDirection(label)== False:
            print(f"edge {label} is undirected")

#Method: getVisited
#Returns True if vertex is visited          
    def getVisited(self,v):
        for vertex in self.vertices:
            if vertex.label ==v:
                return vertex.visited
#Method: setVisited
#Sets vertex to visited 
    def setVisited(self,v):
        for vertex in self.vertices:
            if vertex.label ==v:
                vertex.setVisited()
    
#Method: adjacentPath
#Function for getting the adjacent vertices

    def adjacentEdges(self,vertex): 
        adjacentVal = ""
        for vertices in self.vertices:
            if vertices.label == vertex:
                for edges in vertices.edgeList:
                    adjacentVal = adjacentVal + edges.getTo()

        return adjacentVal

#Method: DepthFirstSearch
#Algorithm that visits every vertex
    def DepthFirstSearch(self, node,visited =DSALinkedList()): #working but different to psuedocode in prac #used linked list to store visited values# code adapted from  https://favtutor.com/blogs/depth-first-search-python
        stack = DSAStack()
        stack.push(node)
        while not stack.isEmpty():
            if node not in visited:
                visited.insertLast(node) #inserting into linked list
                stack.push(node)
                for k in self.getVertex(node).getAdjacent(): #finds the adjacent values of the vertex each time it recurses
                    self.DepthFirstSearch(k,visited) #recursion used to keep going through the function until all nodes visited
            stack.pop()
        return visited #returns the linked list
    
#Method: BreadthFirstSearch
#Algorithm that visits every vertex
    def BreadthFirstSearch(self,start):  #BFS algorithm based on prac6 pseudocode
        T =DSAQueue()
        Q = DSAQueue()
        path = DSALinkedList()
        path.insertLast(start)
        for vertex in self.vertices:
            vertex.clearVisited()
        v=self.getVertex(start)
        self.setVisited(str(v))
        Q.enqueue(v)
        while not Q.isEmpty():
            v = Q.dequeue()
            for w in self.adjacentEdges(str(v)):
                if self.getVisited(w)==False: 
                    T.enqueue(v)
                    T.enqueue(w)
                    self.setVisited(w)
                    Q.enqueue(w)
                    path.insertLast(w)
        return path



    
#Method: pathRec
#Algorithm that returns a path depending on start and destination    
    def pathRec(self, start,dest,visited =DSALinkedList()): #finds a path from start to end #doesnt find shortest path however # extension of DFS
        stack = DSAStack()
        stack.push(start)
        endloop = False

        while not stack.isEmpty() and endloop ==False:  
            if dest in visited:
                endloop == True
                
            elif start not in visited:
                
                visited.insertLast(start)
                stack.push(start)

                for k in self.getVertex(start).getAdjacent():
                    self.pathRec(k,dest,visited)             
            
            stack.pop()
             
        return visited
        
#Method: path
#Algorithm that returns a path depending on start and destination  
# Wrapper for pathRec  
    def path(self,start, end): #wrapper to make it cleaner #returns a long path 
        path =''
        for i in self.pathRec(start, end,visited =DSALinkedList()):
            path+= '-->'+ i 
        return path

#Method: shortestPath
#Algorithm that returns the shortest path depending on start and destination  
# Based off BFS #returns the shortest path 
#Python in Wonderland. 2017. “How to Implement Breadth-First Search in Python.” Python in Wonderland. March 18, 2017. https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/.
    def shortestPath(self,start,end): # algorithm inspired by the code from the web however i have changed it to not use ADTs and to fit with my code  
        visited =DSALinkedList()    
        queue = DSAQueue()
        queue.enqueue(start)
        new_path = ''
        while not queue.isEmpty():
            path = queue.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                for adjacent in self.getVertex(vertex).getAdjacent():
                        new_path = path
                        new_path+="-->"+adjacent
                        queue.enqueue(new_path)   
                        if adjacent == end:
                            return new_path 
                visited.insertLast(vertex)

#Method: BreadthFirstSearchLongestPath
#Algorithm that returns the a path depending on start and destination  
    def BreadthFirstSearchLongestPath(self,start,end):  #BFS algorithm from start to end node# gives long path
        T =DSAQueue()
        Q = DSAQueue()
        path = DSALinkedList()
        path.insertLast(start)
        for vertices in self.vertices:
            vertices.clearVisited()
        v=self.getVertex(start)
        self.setVisited(str(v))
        Q.enqueue(v)
        while not Q.isEmpty():
            v = Q.dequeue()
            for w in self.adjacentEdges(str(v)):
                if self.getVisited(w)==False:
                    T.enqueue(v)
                    T.enqueue(w)
                    self.setVisited(w)
                    Q.enqueue(w)
                    path.insertLast(w)
                if w == end:
                    return path 
        return path

#Method: BFSPath
#Wrapper for BreadthFirstSearchLongestPath    
    def BFSPath(self,start,end):
        path =''
        for i in self.BreadthFirstSearchLongestPath(start,end):
            path+= '-->'+ i 
        return path
