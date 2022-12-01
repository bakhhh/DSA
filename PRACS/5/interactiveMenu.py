from DSATree import *
import pickle

class menu():
    def __init__(self):
        self.tree = BinarySearchTree()
        self.name = None
    
    def printinorder(self):
        return self.tree.inorder()

    def count(self):
        return self.tree.count

    def readCSV(self):
        filename = str(input("Enter a csv file to read from: "))
        with open(filename, 'r') as file:
            for line in file.readline().split(",")[:-1]:
                self.tree.insert(int(line.strip(",")), line)
         
    def readSerialised(self):
        filename = input("Enter serialised file to read: ")
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
      
            for i in obj:
                self.tree.insert(i,i)
        except:
            print("Error: Object file doesnt exist")
       
    def display(self):
        
        print(f"\nDisplaying ......\n", self.order())
        print(".....................")

    def writeCSV(self):
        filename = str(input("Enter a csv file to write to: "))
        display = self.order()
        with open(filename, 'w') as file:
            for  i in display:
                file.write('%d' % i + ',')
  
    def writeSerialised(self):
        filename = input("Enter serialised file to write to: ")
        try:
            with open(filename, "wb") as file:
                pickle.dump(self.tree.inorder(), file)
        except:
            print("Error: Problem picking object")

    def insert(self,key,value):
        return self.tree.insert(key,value)
    def delete(self,value):
        return self.tree.delete(value)

    def order(self):
        getOrder = int(input("InOrder....[1]\nPreOrder....[2]\nPostOrder....[3]\n\nSelect an option: "))
        if getOrder == 1:
            return self.tree.inorder()
        elif getOrder == 2: 
            return self.tree.preOrder()
        elif getOrder == 3:
            return self.tree.postOrder()
        else:
            print("Invalid Option selected")

    def userInterface(self):
        getInput = str(input("\nInsert....[1]\nDelete....[2]\nDisplay....[3]\nWrite Serialised File....[4]\nWrite to CSV....[5]\nRead Serialised File....[6]\nRead from CSV....[7]\nExit(X)\n\nPlease Select an option: "))
        return getInput.lower()

def main():
    imenu = menu()
    while True:
        userInput = None
        if userInput != "x":
            userInput = imenu.userInterface()
        if userInput == "1":
            print("Insert selected.....")
            value = (input("Enter value to insert: "))
            imenu.insert(int(value),value)

        elif userInput == "2":
            try:
                if imenu.tree.count ==0:
                    raise ValueError("Tree is empty")
                else:
                    print("Delete selected.....")
                    key = input(f"Pick value to delete: {imenu.printinorder()} :")
                    imenu.delete(int(key))

            except Exception as e:
                print("Error: ",e)


        elif userInput == '3':
            try:
                if imenu.tree.count ==0:
                    raise ValueError("Tree is empty")
                else:
                    print("\nDisplay selected.....\n")
                    imenu.display()
            except Exception as e:
                print("Error: ",e)

        elif userInput == '4':
                print("\Write to Serialised selected.....\n")
                imenu.writeSerialised()
            
        elif userInput == '5':
            print("\Write to CSV selected.....\n")
            imenu.writeCSV()

        elif userInput == '6':
            print("\Read Serialised selected.....\n")
            imenu.readSerialised()

        elif userInput == '7':
            print("\Read CSV selected.....\n")
            imenu.readCSV()

        elif userInput == "x":
            return False
            
main()