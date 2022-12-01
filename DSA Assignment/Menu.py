#File: #Menu.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 3/4/22
#Data Structures & Algorithms Assignment
from Keyboard import *
from myException import * #custom exceptions

#Class Menu   
# Interactive menu     
class menu:
    def __init__(self):
        self.keyboard = keyboard() #seting self.keyboard as the keyboard class

#Method: userInterface
#Displays the menu options 



#Method: interactive
#Interactive menu
#Allows you to select from userInterface options
    def interactive(self): #base code updated from pracs 4, 5, 6
        endLoop = False
        while endLoop == False:
            getInput = None
            if getInput != "x":    #while the input is not x return the menu
                getInput = self.userInterface()
            if getInput == "1": #if the input is 1 it allows you to load a keyboard file of choice
                inp = None
                while inp != 'x': # another while loop to select between loading a regular file or serialised file
                    inp= input("\nRead Keyboard File [1]\nRead Serialised File [2]\nExit [x]\n\nSelect an option: ")
                    if inp == '1':
                        filename = input("Enter a file to load keyboard: ")
                        self.keyboard.insertIntoGraph(filename)
                    if inp == '2':
                        filename = input("\nEnter a filename to unserialise keyboard: ")   
                        self.keyboard.unpickleFile(filename)                        
               
            elif getInput == "2": #if input is 2 node operations will be selected
                inp= None
                while inp != 'x':
                    inp= input("\nFind [1]\nInsert [2]\nDelete [3]\nUpdate [4]\nExit [x]\n\nSelect an option: ")
                    if inp == '1':
                        v= str(input("Enter a Vertex to find: "))
                        f = self.keyboard.findVertex(v) #find vertex
                    elif inp == '2':
                        v= input("Enter a Vertex to insert: ")
                        self.keyboard.insertVertex(v) #insert vertex
                    elif inp == '3':
                        v= str(input("Enter a Vertex to delete: "))
                        self.keyboard.deleteVertex(v)        #delete vertex
                    elif inp == '4':
                        oldVertex = (input("Enter a vertex to update: "))
                        newVertex = (input("What would you like to change it to: "))
                        self.keyboard.updateVertex(oldVertex,newVertex)            #update vertex

            elif getInput == "3": #if input 3 edge operations will be selected
                inp= None
                while inp != 'x':
                    inp= input("\nfind [1]\nAdd [2]\nDelete [3]\nUpdate [4]\nExit [x]\n\nSelect an option: ")
                    if inp == '1':
                        e1= str(input("Enter vertex 1: "))
                        e2 = str(input("Enter vertex 2: "))
                        self.keyboard.findEdge(e1,e2) #find edge
                        
                    elif inp == '2':
                        e1= str(input("Enter vertex 1: "))
                        e2 = str(input("Enter vertex 2: "))
                        weight = str(input("Enter weight for edge: "))
                        directed = str(input("\nDirected [1]\nUndirected[2]\nPlease Select An Option: "))
                        if directed == '1':
                            direction = True
                        elif directed == '2':
                            direction = False
                        self.keyboard.insertEdge(e1,e2,weight,direction) #insert edge
                    elif inp == '3':
                        e1= str(input("Enter vertex 1: "))
                        e2 = str(input("Enter vertex 2: "))
                        self.keyboard.deleteEdge(e1,e2)  #delete edge

                    elif inp == '4':
                        getInput = input("\nUpdate Edge [1]\nUpdate Weight [2]\nUpdate Direction [3]\n\nWhat would you like to update: ")

                        if getInput== '1':
                            edge =input("Enter an Edge to change: ")
                            new1 = input("Enter a Vertex : ")
                            new2 = input(f"Enter a Vertex to connect {new1} to: ")
                            if self.keyboard.graph.findEdge(new1,new2) == False:
                                self.keyboard.updateEdge(edge,new1,new2)
                                print(f"Edge {edge} updated to {new1+new2} ")
                            else:
                                print(f"\nEdge {edge} cant be updated to {new1+new2} as edge already exits")
                            
                        elif getInput=='2':
                            v1 = input("Enter a Vertex: ")
                            v2 = input(f"Enter a Vertex connected to {v1}: ")
                            weight = input("What would you like to change the weight to: ")
                            self.keyboard.updateWeight(v1,v2,weight)
                                
                        elif getInput=='3':
                            v1 = input("Enter a Vertex: ")
                            v2 = input(f"Enter a Vertex connected to {v1}: ")
                            self.keyboard.updateDirection(v1,v2)

            elif getInput == "4": #if input is 4 then display graph as adjacency list and matrix
                try:
                    if self.keyboard.graph.getVertexCount()== 0:
                        raise valueError("Graph is empty")
                    else:
                        print("\nDisplaying Keyboard as List: \n")
                        self.keyboard.graph.displayAsList()
                        print("\nDisplaying Keyboard as Matrix: \n")
                        self.keyboard.graph.displayAsMatrix()
                except valueError as e:
                    print("Error", e)

            elif getInput == "5": #if input is 5 then display graph information such as number of edges/vertexs, weight, direction
                print("\n---DISPLAYING GRAPH INFORMATION---\n")
                for edges in self.keyboard.graph.edges:
                    print(f"Edge = {edges} : Weight = {edges.weight} : Directed[TRUE]/Undirected[FALSE] = {edges.getDirected()} ")
                print("\nEdge Count = ",self.keyboard.graph.getEdgeCount())
                print("\nVertex Count = ",self.keyboard.graph.getVertexCount())
                print("\n---DISPLAYING COMPLETE---\n")
            
            elif getInput == "6": #if input is 6 you can find the shortest path of a string 
                try:
                    if self.keyboard.graph.vertices.count != 0:
                        string = str(input("Enter a string to find path: "))
                        self.keyboard.findShortestPath(string)
                    else:
                        raise valueError("Error: Cant generate paths without vertices and edges")
                except valueError as e:
                    print(e)

            elif getInput == "7": #if input is 7 generate paths #this wont display paths but instead generates the paths into a text file
                try:
                    if self.keyboard.graph.vertices.count != 0:
                        string = str(input("Enter a string to find path: "))
                        self.keyboard.findStringPath(string)
                        # self.keyboard.generatePaths(string)
                        print("\n---PATHS GENERATED---\n")
                    else:
                        raise valueError("Error: Cant generate paths without vertices and edges")
                except valueError as e:
                    print(e)

            elif getInput == "8": #if input is 8 it will display the generate paths in order
                try:
                    if self.keyboard.graph.vertices.count != 0:
                        count=0
                        content =self.keyboard.displayInOrder()
                        print("\nPATHS RANKED IN ORDER\n")
                        for line in content:
                            count+=1
                            print(f"{count}: " "%s\n" % line)
                        inp =None
                        while inp !='x':
                            inp= input("\nSave Sorted Paths to file [1]\nExit[x]\n\nSelect an option: ")
                            if inp == '1':
                                filename = input("\nEnter a file to save to: ")
                                self.keyboard.writeSortedPathsToFile(filename)
                            if inp != '1':
                                print("Incorrect input ")

                    else:
                        raise valueError("Error: Cant find path without vertices and edges")
                except valueError as e:
                    print(e)

            elif getInput == "9": #if input is 9 it saves keyboard into a serialised file where it can be loaded up again
                filename = input("\nEnter a file to save keyboard as serialised file: ")
                self.keyboard.saveKeyboard(filename)

            elif getInput == "x": #exits the program
                endLoop = True
            
            else:
                print("Error: Invalid Input")