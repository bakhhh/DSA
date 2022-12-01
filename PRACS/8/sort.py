from minHeap import *


def readWrite():
    heap =DSAHeap(7000)
    with open('RandomNames7000.csv', 'r') as file:
        for line in file:
            heap.add(line.split(",")[0],line.split(",")[0])
        heap.heapSort()
    with open('output.txt', 'w') as file:
        for i in range(heap.count):
            file.write("%s\n" % heap.heapArray[i].priority)




readWrite()
