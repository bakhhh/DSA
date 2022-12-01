#
# Data Structures and Algorithms COMP1002
#
#prac11

# Sohail Bakhshi 
# Student ID - 20605126
import unittest
import random as r

def printList(A):
    for i in range(len(A)):
        print(A[i], end=" ")
    print()

def shellSort(A):
    interval = len(A) // 2
    while interval > 0:
        for i in range(interval, len(A)):
            temp = A[i]
            j = i
            while j >= interval and A[j - interval] > temp:
                A[j] = A[j - interval]
                j -= interval

            A[j] = temp
        interval //= 2

def countingSort(A):
    max_element = int(max(A))
    min_element = int(min(A))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(A))]
  
    for i in range(0, len(A)):
        count_arr[A[i]-min_element] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
  
   
    for i in range(len(A)-1, -1, -1):
        output_arr[count_arr[A[i] - min_element] - 1] = A[i]
        count_arr[A[i] - min_element] -= 1
  
    for i in range(0, len(A)):
        A[i] = output_arr[i]
  
    return A

 
# Method to do Radix Sort
def radixSort(arr):
    max1 = max(arr)
    while max1 / exp >= 1:
        countingSort(arr)
        exp *= 10
 

class testSort(unittest.TestCase):

    def testShellSort(self):
        arr = []
        for i in range(20):
            n = r.randint(1,100)
            arr.append(n)
        print("")
        printList(arr)
        shellSort(arr)
        printList(arr)

    def testCountSort(self):
        arr = []
        for i in range(20):
            n = r.randint(1,100)
            arr.append(n)
        print("")
        printList(arr)
        countingSort(arr)
        printList(arr)


    def testRadixSort(self):
        arr = []
        for i in range(20):
            n = r.randint(1,100)
            arr.append(n)
        print("")
        printList(arr)
        radixSort(arr)
        printList(arr)
        



if __name__ == "__main__":
    unittest.main()