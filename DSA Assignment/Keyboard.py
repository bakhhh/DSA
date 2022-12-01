#File: #keyboard.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 7/4/22
#Data Structures & Algorithms Assignment

import pickle
from DSAGraph import * #Previously submitted for Practical 6 in COMP1002, Sem 2, 2022
import numpy as np
from myException import*

#Class Keyboard
#Contains all the functions for the interative menu
class keyboard:
    def __init__(self):
        self.graph = DSAGraph() #setting self.graph as my graph class

#Method: lengthOfCol
#returns the amount of columns there is in a file
    def lengthOfCol(self,filename):
        with open(filename, 'r') as file:
            for line in file:
                content = line.split()
            arr = np.array(content)
            count = len(arr)
        return count

#Method: lengthOfRow
#returns the amount of rows there is in a file
    def lengthOfRow(self,filename):
        with open(filename, 'r') as file:
            content = file.readlines()
            arr = np.array(content)
            count = len(arr)
        return count
         

#Method: readKeyboard
#reads a keyboard file into an array
    def readKeyboard(self,filename):
        try:
            row = self.lengthOfRow(filename)
            col = self.lengthOfCol(filename)
            with open(filename, 'r') as file:
                array = np.empty([row,col],dtype=object)
                for index, lines in enumerate(file):
                    for i in range(len(lines.split())): 
                        if index ==i :
                                for k in range(len(lines.split())):
                                    array[i][k]= lines.split()[k] #inserting file into a 2d array
                print("\nKeyboard loaded.....\n")
                return array
        except FileNotFoundError as e:
            print(e)


#Method: insertIntoGraph
#Inserts any keyboard file into DSAgraph 
    def insertIntoGraph(self,filename):
            try:
                array =self.readKeyboard(filename)
                for line in array:
                    
                    for vertex in line:
                        val = 0
                        for item in self.graph.vertices: # prevents adding the same vertex twice
                            if item.getLabel() == vertex:
                                val = 1
                        if val == 0:
                            self.graph.addVertex(vertex, vertex)
                    for i in range(len(line)-1):
                        self.graph.addEdge(line[i],line[1+i],1,False)
                        
                for i in range(len(array)-1):
                    for j in range(len(line)):
                        self.graph.addEdge((array[i][j]),(array[i+1][j]),1,False)
                
            except TypeError as e:
                print(e)
#Method: deleteVertex
# Deletes vertex from keyboard/graph
    def deleteVertex(self, value):
        if self.graph.foundVertex(value) == True:
            self.graph.removeVertex(value)
            print(f"\nVertex {value} removed")
        else:
            print("Vertex not found")

#Method: findVertex
# Finds the selected vertex from the graph/keyboard. If vertex not found it should throw an exception(implemented within graph class)     
    def findVertex(self,value):
        found = True
        notfound =False
        if self.graph.findNode(value) == True:
            print(f"Vertex {value} is found in the graph")
            return found
        else:
            return notfound
        

#Method: insertVertex
# Inserts a vertex into the keyboard/graph      
    def insertVertex(self, value):
        if self.graph.foundVertex(value) == True:
            print(f"Vertex {value} is already in the graph")
        else:
            print(f"Vertex {value} is inserted into the graph")
            self.graph.addVertex(value,value)

#Method: updateVertex
# Updates the selected vertexs name      
    def updateVertex(self,oldVertex,newVertex):
        if self.graph.foundVertex(oldVertex) == True:
            self.graph.updateVertex(oldVertex,newVertex)
            print(f"Vertex {oldVertex} updated to {newVertex} ")
        else:
            print(f"Vertex {oldVertex} not found")

#Method: deleteEdge
# Inserts a vertex into the keyboard/graph   
    def deleteEdge(self,label1,label2):
        self.graph.removeEdge(label1,label2)
        print(f"\nEdge {label1+label2} removed")

#Method: findEdge
# Finds an edge in the keyboard/graph if not found exception is thrown     
    def findEdge(self,label1, label2):
        val =''
        found = True
        notfound =False
        if self.graph.checkEdge(label1+label2) == True:
            val = label1+label2
            print(f"\nEdge {val} is found in the graph")
            return found
        else:
            return notfound 
         
#Method: insertEdge
# Inserts an edge into the keyboard/graph. Also checks if edge is already in the graph
    def insertEdge(self,label1,label2,weight,directed):
        if self.graph.findEdge(label1,label2) ==False:
            self.graph.addEdge(label1,label2,weight,directed)
            print(f"\nEdge {label1+label2} added to the graph")
        else:
            print(f"\nEdge {label1+label2} is already in the graph")

#Method: updateEdge
# Allows you to change the edge label
    def updateEdge(self,edge,v1,v2):
        self.graph.updateEdge(edge,v1,v2)

#Method: updateWeight
# Allows you to change the edge weight 
    def updateWeight(self,v1,v2,weight):
        self.graph.updateWeight(v1,v2,weight)

#Method: updateDirection
# Allows you to change the edge direction
    def updateDirection(self,v1,v2):
        self.graph.updateDirection(v1,v2)
        
#Method: findPath
# Writes 3 different paths into a file for a string based on 3 algorithms
    def findStringPath(self,string):
        val = ''
        val2 =''
        val3 =''
        print("\n--- Finding string path ---\n")
        for i in range(len(string)-1):
            val +=self.graph.path(string[i] , string[i+1])
            val2 +=self.graph.shortestPath(string[i] , string[i+1])
            val3 += self.graph.BFSPath(string[i] , string[i+1])
        with open('paths.txt','w') as file:
            file.write("%s\n" % val )
            file.write("%s\n" % val2 )
            file.write("%s\n" % val3 )

#Method: getPath
# Writes 3 different paths into a file for each string in a file
    def getPath(self,filename):
        try:
            path1 = ''
            path2 =''
            path3 =''
            with open(filename, 'r') as file:
                content = file.read().split()
                contentArray = np.array(content) #putting the content into an array
                for word in contentArray:

                    for letter in range(len(word)-1):
                        path1 += self.graph.path(word[letter] , word[letter+1])  
                        path2 +=self.graph.shortestPath(word[letter] , word[letter+1])
                        path3 += self.graph.BFSPath(word[letter] , word[letter+1])       
                    path1+='\n'
                    path2+='\n'
                    path3+='\n'
                        
            with open('paths.txt','w') as file:
                file.write("%s\n" % path1 )
                file.write("%s\n" % path2 )
                file.write("%s\n" % path3 )
        except FileNotFoundError as e:
            print(e)
        
    
#Method: findShortestPath
# Returns the shortest path
    def findShortestPath(self,string):
        path = ''
        print("\n--- Finding Shortest path ---\n")
        for i in range(len(string)-1):
            path +=self.graph.shortestPath(string[i] , string[i+1]) 

        print(f"Shortest Path for string = {path}")
        return path
            

#Method: selectionSort
# Sorts out the path based on length
#modified selection sort
#Previously submitted for Practical 1 in COMP1002, Sem 2, 2022
    def selectionSort(self, A):
        for i in range(len(A)):  
            min = i
            for j in range(i+1,len(A)): # range of elements to the right of i to the length of A
                if len(A[j]) < len(A[min]):         #if the value of a number in k is less than a value in i then swap
                    min = j  
            temp = A[min]  #swap numbers
            A[min]= A[i]
            A[i] = temp
        return A

#Method: displayInOrder
# Returns the paths sorted in order      
    def displayInOrder(self):
        with open('paths.txt','r') as file:
            content = file.read().split()
            array = np.array(content) #putting content in an array
        self.selectionSort(array)
        return array

#Method: writeSortedPathsToFile
# Writes the sorted paths into a file of choice         
    def writeSortedPathsToFile(self,filename):
        count=0
        sorted = self.displayInOrder()
        with open(filename,'w') as file:
            file.write("Rankings\n")
            for line in sorted:
                count+=1
                file.write(f"{count}: " "%s\n" % line)

#Method: saveKeyboard
# Saves the current keyboard file as a serialised file 
    def saveKeyboard(self,filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self.graph, file)
        except:
            print("Error: Problem picking object")

#Method: unpickleFile
# Allows you to load serialised file 
    def unpickleFile(self,filename):
        try:
            with open(filename, "rb") as file:
                keyboard = pickle.load(file)
            self.graph = keyboard
            print("\nKeyboard loaded.....\n")
        except:
            print("Error: Object file doesnt exist")