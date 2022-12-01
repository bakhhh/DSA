# Sohail Bakhshi 
# Student ID - 20605126
from DSAsorts import bubbleSort, insertionSort, selectionSort

import numpy as np 

def choseSortingAlgo(getinput, array):

    if getinput[0].lower() == 'b':
        print("bubbleSort Selected")
        bubbleSort(array)
        
    elif getinput[0].lower() == 'i':
        print("InsertionSort Selected")
        insertionSort(array)
        

    elif getinput[0].lower() == 's':
        print("SelectionSort Selected")
        selectionSort(array)
        
    else:
        print("Invalid Command ")
        exit()
        
def readinglines(getinput):
    list1 = []
    with open('RandomNames7000.csv', 'r') as file:
        for line in file:
            list1.append(line.split(",")[0])
            anArray = np.array(list1)
    choseSortingAlgo(getinput, anArray)
    return anArray

def writeLines(filename,getinput):
    anArray = readinglines(getinput)

    with open(filename, 'w') as file:
        for lines in anArray:
            file.write("%s\n" % lines)


def main():
    
    
    getinput = input('Please Chose a sorting Algorithim:\n(B)ubbleSort, (S)electionSort, (I)nsertionSort : ')
    filename = input("Please Enter a Filename.csv:  ")
    readinglines(getinput)
    writeLines(filename, getinput)



main()



