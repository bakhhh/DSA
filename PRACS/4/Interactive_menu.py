import pickle
from linkedLists import *

class menu:

    def __init__(self):
        self.ll = DSALinkedList()

    def read(self): #reading serialized txt
        filename = input("Enter a file to read from: ")
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            for i in obj:
                self.ll.insertLast(i)
        except:
            print("Error: Object file doesnt exist")

    def write(self): #writing a serialized text
        filename = input("Enter a file to write to: ")
        try:
            with open(filename, "wb") as file:
                pickle.dump(self.ll, file)
        except:
            print("Error: Problem picking object")

    def insertFirst(self):
        value = input("Enter a value to insert at the front of the list: ")
        self.ll.insertFirst(value)

    def insertLast(self):
        value = input("Enter a value to insert at the end of the list: ")
        self.ll.insertLast(value)

    def removeLast(self):
        return self.ll.removeLast()

    def removeFirst(self):
        return self.ll.removeFirst()

    def display(self):
        print("----------------")
        if self.ll.isEmpty()==True:
            print("No items in the list")
        else:
            for i in self.ll:
                print(i)
        print("----------------")
    def userIn(self):
        getInput = str(input("\nInsertFirst(if)\nInsertLast(il)\nRemoveFirst(rf)\nRemoveLast(rl)\nDisplay list(d)\nWrite Serialised File(w) \nRead Serialised File(r)\nExit Program(x)\n\nPlease Chose an option: "))
        return getInput.lower()


def main():
    imenu = menu()
    while True:
        userInput = None
        if userInput != "x":
            userInput = imenu.userIn()
        if userInput == "if":
            print("Insert first selected.......")
            imenu.insertFirst()

        elif userInput== "il":
            print("Insert Last selected.......")
            imenu.insertLast()

        elif userInput == "rf":
            print("Remove first selected.......")
            imenu.removeFirst()
        
        elif userInput == "rl":
            print("Remove Last selected.......")
            imenu.removeLast()
            
        elif userInput == "d":
            print("Display selected.......")
            imenu.display()

        elif userInput == "w":
            print("Write selected.......")
            imenu.write()

        elif userInput == "r":
            print("Read selected.......")
            imenu.read()

        elif userInput == "x":
            return False
    
            


main()

    