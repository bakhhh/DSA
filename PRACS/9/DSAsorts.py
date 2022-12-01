#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
# Sohail Bakhshi 
# Student ID - 20605126
import unittest
import numpy as np
import random as r

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


def recCall(A,left, right, level =1):
    space = '      '
    indnt = level*space # allows indentation for each level
    print(f"{indnt} Recursion Level = {level}")
    print(f"{indnt} mergeSort({A})")
    print(f'{indnt} mergeRec({left}, {right})')

def mergeCall(A,left,mid, right, level =1):
    space = '      '
    indnt = level*space # allows indentation for each level
    print(f'{indnt} merge({left}, {mid}, {right})')

def recQuicksortCall(A,left, right, level):
    space = '      '
    indnt = level*space # allows indentation for each level
    print(f"{indnt} Recursion Level = {level}")
    print(f"{indnt} q_rec({A})")
    print(f'{indnt} quickSort(A, {left}, {right})')

def recPartionCall(left, right, pivot, level):
    space = '      '
    indnt = level*space # allows indentation for each level
    print(f'{indnt} doPart(A, {left}, {right}, {pivot})')

def mergeSort(A):
    mergeSortRecurse(A, 0, len(A) - 1)
    

def mergeSortRecurse(A, leftIndex, rightIndex,level=1):
    if leftIndex < rightIndex:
        midIdx = (leftIndex + rightIndex)//2
        recCall(A,leftIndex,rightIndex,level)
        mergeCall(A,leftIndex,midIdx,rightIndex,level)
        print('')
        mergeSortRecurse(A, leftIndex, midIdx,level+1)

        mergeSortRecurse(A, midIdx + 1, rightIndex,level+1)
        
        merge(A, leftIndex, midIdx, rightIndex,level+1)
        

        


def merge(A, left, mid, right,level=1):
    tempArr = np.zeros(right - left + 1, dtype=object)
    i = left
    j = mid + 1
    k = 0

    while (i <= mid) and (j <= right): 
        if A[i] <= A[j]:
            tempArr[k] = A[i]
            i+=1
        else:
            tempArr[k] = A[j]
            j += 1 
        k += 1
    for i in range(i, mid+1, 1):
        tempArr[k] = A[i]
        k += 1
    for j in range(j, right+1, 1):
        tempArr[k] = A[j]
        k += 1

    for k in range(left, right + 1, 1):
        A[k] = tempArr[k-left]
    


def quickSort(A):
    quickSortRecurse(A,0,len(A)-1,1)

def quickSortMedian3(A):
    quickSortRecurse(A, 0, len(A)-1,2)

def quickSortLeft(A):
    quickSortLeftRecurse(A,0,len(A)-1)

def quickSortRandom(A):
    quickSortRecurse(A,0,len(A)-1,4)

def quickSortLeftRecurse(A, leftIdx, rightIdx,level=1):
    if rightIdx > leftIdx:
        pivotIdx = (rightIdx)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        recQuicksortCall(A,leftIdx,rightIdx,level)
        recPartionCall(leftIdx, rightIdx, pivotIdx,level) 
        print('')
        quickSortLeftRecurse(A, leftIdx, newPivotIdx-1,level+1)
        quickSortLeftRecurse(A, newPivotIdx + 1, rightIdx,level+1)

def returnRandom(left,right,mid):
    A = r.choice([left,mid,right])
    return A

def quickSortRecurse(A, left, right,num):
    if num ==1:
        if right > left:
            pivot = (left + right)//2
            newPivot = doPartitioning(A, left, right, pivot)
            quickSortRecurse(A, left, newPivot-1,num)
            quickSortRecurse(A, newPivot + 1, right,num)
    if num ==2:
        if right > left:
            mid = (left + right)//2
            pivot = median_of_three(A, left, mid, right)
            newPivot = doPartitioning(A, left, right, pivot)
            quickSortRecurse(A, left, newPivot-1,num)
            quickSortRecurse(A, newPivot + 1, right,num)
    if num ==3:
        if right > left:
            pivot = left
            newPivot = doPartitioning(A, left, right, pivot)
            quickSortRecurse(A, left, newPivot-1,num)
            quickSortRecurse(A, newPivot + 1, right,num)
    if num ==4:
        if right > left:
            mid = (left + right)//2 
            pivot = returnRandom(left,mid,right)
            newPivot = doPartitioning(A, left, right, pivot)
            quickSortRecurse(A, left, newPivot-1,num)
            quickSortRecurse(A, newPivot + 1, right,num)


def doPartitioning(A, leftIdx, rightIdx, pivIdx,level=1):
    pivotVal = A[pivIdx]
    A[pivIdx] = A[rightIdx]
    A[rightIdx] = pivotVal

    currIdx = leftIdx

    for ii in range(leftIdx, rightIdx):
        if A[ii] < pivotVal:
            temp = A[ii]
            A[ii] = A[currIdx]
            A[currIdx] = temp
            currIdx += 1
    
    newPivIdx = currIdx
    A[rightIdx] = A[newPivIdx]
    A[newPivIdx] = pivotVal

    return newPivIdx


def median_of_three(A, left, mid, right):
    if A[left] >= A[mid] and A[left] <= A[right]:
        return left
    elif A[left] >= A[right] and A[left] <= A[mid]:
        return left
    if A[mid] >= A[left] and A[mid] <= A[right]:
        return mid
    elif A[mid] >= A[right] and A[mid] <= A[left]:
        return mid
    if A[right] >= A[left] and A[right] <= A[mid]:
        return right
    elif A[right] >= A[mid] and A[right] <= A[left]:
        return right

 
def printList(A):
    for i in range(len(A)):
        print(A[i], end=" ")
    print()



class testSort(unittest.TestCase):

    # def testMergeSort(self):
    #     randomlist = [2,0,6,0,5,1,2,6]
    #     printList(randomlist)
    #     mergeSort(randomlist)
    #     printList(randomlist)

    # def testQuickSort(self):
    #     arr =[13, 31, 34 ,3, 68, 36, 35 ,85 ,35, 46 ,256, 8 ,93 ,9, 1 ]
    #     printList(arr)
    #     quickSort(arr)
    #     printList(arr)

    # def testQuickSortmed(self):
    #     arr =[13, 31, 34 ,3, 68, 36, 35 ,85 ,35, 46 ,256, 8 ,93 ,9, 1 ]
    #     printList(arr)
    #     quickSortMedian3(arr)
    #     printList(arr)

    def testQuickSortleft(self):
        randomlist = [0,0,1,2,2,5,6,6]
        # for i in range(0,20):
        #     n = r.randint(1,100)
        #     randomlist.append(n)
    
        printList(randomlist)
        quickSortLeft(randomlist)
        printList(randomlist)

    # def testQuickSortRandom(self):
    #     arr =[13, 31, 34 ,3, 68, 36, 35 ,85 ,35, 46 ,256, 8 ,93 ,9, 1 ]
    #     printList(arr)
    #     quickSortRandom(arr)
    #     printList(arr)

if __name__ == "__main__":
    unittest.main()