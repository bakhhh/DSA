#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
# Sohail Bakhshi 
# Student ID - 20605126
# The following algorithim codes were inspired by the pseudocode in Lecture 1


def bubbleSort(A):
    sort = False
    while sort != True: # while swapped does not = true
        sort = True  # break from loop once the algorithm has sorted all the numbers
        for i in range(0, len(A)-1):  # for every value in the list
            if A[i] > A[i+1]: #if the left is greater than the right variable
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp# swap the values
                sort = False #numbers are not sorted yet
                   
    return A
                    


def insertionSort(A):
    for i in range(1, len(A)): #range between 1 and the length of A
        unsorted_num = A[i]
        while A[i-1] > unsorted_num and i>0: # while value to left is greater than value to the right and i = greater than 0 to prevent negative indexing
            temp = A[i]
            A[i]= A[i-1]
            A[i-1]= temp  #swapping the 2 values
            i = i -1 #stepping down the list

    return A


def selectionSort(A):
    for i in range(0, len(A)):  
        min = i
        for j in range(i+1,len(A)): # range of elements to the right of i to the length of A
            if A[j] < A[min]:         #if the value of a number in k is less than a value in i then swap
                min = j  
        temp = A[min]  #swap numbers
        A[min]= A[i]
        A[i] = temp
    return A


def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


# def main():
#     num = [3, 9, 5, 6, 1, 4, 22, 1 ,44, 0]
#     selectionSort(num)

#     print(num)

# main()

