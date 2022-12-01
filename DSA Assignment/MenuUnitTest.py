#File: #MenuUnitTest.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 9/4/22
#Data Structures & Algorithms Assignment
import unittest
from Menu import *


#allows you to load the interactive menu to test each option

##to test interactive mode

#Enter 1 to  load a keyboard file
#Enter 2 to  enter node operations
#Enter 3 to  enter edge operations
#Enter 4 to display graph (if no keyboard loaded then error message will display)
#Enter 5 to display graph information (if no keyboard loaded then error message will display)
#Enter 6 to display the shortest path of a string (if no keyboard loaded then error message will display)
#Enter 7 to generate 3 paths of a string (if no keyboard loaded then error message will display)
#Enter 8 to display the generated paths of a string (if no keyboard loaded then error message will display)
#Enter 9 to save serialised keyboard
#Enter x to exit program
#Enter a random integer/string that is not the numbers 1-9 and x (should return an error message(You might have to enlarge the terminal to see it if you cant))

#to test keyboard loading 
##Enter 1 to  load a keyboard file
#Enter 1 to read keyboard file
#Enter 2 to read serialised file
#If file doesnt exit an error should be displayed other wise keyboard loaded will be displayed

#to test node operations
#Enter 2 to  enter node operations
#Enter 1 to find node (if node not found error should say not found) 
#Enter 2 to insert node (if node already exist error message will be displayed)
#Enter 3 to delete node (if node doesnt exist error message will be displayed)
#Enter 4 to update node (if node doesnt exist error message will be displayed)

#to test edge operations
#Enter 3 to  enter edge operations
#Enter 1 to find edge (if edge not found error should say not found) 
#Enter 2 to add edge (if edge already exist error message will be displayed)
#Enter 3 to delete node (if edge doesnt exist error message will be displayed)
#Enter 4 to update edge (if edge doesnt exist error message will be displayed)

class testMenu(unittest.TestCase):

    def testInteractive(self):
        m= menu()
        m.interactive()
   


if __name__ == "__main__":
    unittest.main()
