from DSAGraph import *


class menu:

    def __init__(self) -> None:
        self.graph = DSAGraph()

    def read(self,filename):
        try:
            with open(filename, "r") as file:
                for lines in file:
                    for i,vertex in enumerate(lines.split()):
                        val = 0
                        for item in self.graph.vertices:
                            if item.getLabel() == vertex:
                                val = 1
                        if val == 0:
                            self.graph.addVertex(vertex, vertex)
                    self.graph.addEdge(lines.split()[0],lines.split()[1])
        except Exception as e:
            print("ERROR ", e)

    def reset(self):
        return self.graph.removeVertex()



    def userInterface(self):
        getInput = str(input("\nDisplay....[1]\nRead from file....[2]\nReset....[3]\nBFS....[4]\nDFS....[5]\nExit(X)\n\nPlease Select an option: "))
        return getInput.lower()


def main():
    imenu = menu()

    while True:
        userInput = None
        if userInput != "x":
            userInput = imenu.userInterface()
        if userInput == "1":
            try: 
                if imenu.graph.getVertexCount() ==0:
                    raise ValueError("Graph is empty")
                else:
                    print("Display selected.....")
                    getInput = str(input("\nDisplay As List....[1]\nDisplay as Matrix....[2]\nExit(X)\n\nPlease Select an option: "))
                    if getInput == '1':
                        imenu.graph.displayAsList()
                    elif getInput == '2':
                        imenu.graph.displayAsMatrix()
                    elif userInput == "x":
                        return False
            except Exception as e:
                print("Error: ", e)
            

        elif userInput == "2":
            print("Read selected.....")
            getInput = str(input("\nPrac6_1.al....[1]\nPrac6_2.al....[2]\nSelect Other....[3]\nExit(X)\n\nPlease Select an option: "))
            if getInput == '1':
                imenu.read('Prac6_1.al')
            elif getInput == '2':
                imenu.read('Prac6_2.al')
            
            elif getInput == '3':
                filename=input("Enter a file name: ")
                imenu.read(filename)
            elif getInput == 'x':
                return False

        elif userInput == "3":
            print("Reset selected.....")
            imenu.reset()
            imenu.reset()

        elif userInput == "4":
            print("Breadth First Search selected.....")
            imenu.graph.BFS()

        elif userInput == "5":
            print("Depth First Search selected.....")
            v = imenu.graph.firstVertex()
            for i in imenu.graph.DFS(v):
                print(i, end='')
           
        elif userInput == "x":
            return False

main()
             