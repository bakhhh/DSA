#File: #keyMeUp.py - main file to run
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 9/10/22
#Data Structures & Algorithms Assignment

import sys
from Menu import *

#keyMeUp class
class keyMeUp:

#Method: errorMessage
# displays usage info if incorrect input     
    def errorMessage(self): #displays usage information
        print("############## USAGE INFORMATION ##################\n")
        print("• Interactive testing environment | keyMeUp.py -i \n")
        print("• Silent mode  | keyMeUp.py -s keyFile strFile pathFile \n")
        print("###################################################")

#Method: mainMenu
# calls functions based on command line argument
    def mainMenu(self):
        imenu = menu()
        if len(sys.argv) == 1:  #if no command line arguments are given
            self.errorMessage()
        elif len(sys.argv) == 2: #enter interactive mode
            if (sys.argv[1]) == "-i":
                imenu.interactive()
            else:
                print("Invalid Argument")
                self.errorMessage()
        elif len(sys.argv) == 5:  #silent mode
            if (sys.argv[1]) == "-s":
                try:
                    filename = sys.argv[2]
                    imenu.keyboard.insertIntoGraph(filename)
                    stringFile =sys.argv[3]
                    imenu.keyboard.getPath(stringFile)
                    output =sys.argv[4]
                    imenu.keyboard.writeSortedPathsToFile(output)
                except AttributeError as e:
                    print(e)

            else:
                print("Invalid Argument")
                self.errorMessage()
        else:
            print("\nInvalid Argument Entered\n")
            self.errorMessage()

assignment = keyMeUp()
assignment.mainMenu()