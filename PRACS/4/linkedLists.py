class DSAListNode:
    def __init__(self, value:object):
        self.value = value
        self.next = None
        self.prev= None

    def getValue(self):
        return self.value

    def setValue(self, inValue):
        self.value = inValue

    def getNext(self):
        return self.next        

    def getPrev(self):
        return self.prev

    def setNext(self, newNext):
        self.next = newNext
    
    def setPrev(self, prev):
        self.prev = prev


class DSALinkedList(DSAListNode):
  
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __iter__(self):   #Lecture 4 slide 72
        curNd = self.head
        while curNd != None:
            yield curNd.value
            curNd = curNd.next

    def __next__(self):
        return self

    def getCount(self):
        return self.count
        
    def getTail(self):
        return self.tail
    
    def insertFirst(self, value):
        newNd = DSAListNode(value)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
            # newNd.setPrev(None)
            # newNd.setNext(None)
        else:
            self.head.prev = newNd 
            newNd.next = self.head
            self.head = newNd
            
            # newNd.setPrev(None)
            # currNd = self.head
            # while currNd.getNext() != None:
            #     currNd = currNd.getNext()
            # # currNd.next = None
            # self.tail = currNd
        self.count += 1

        
    def insertLast(self, value):
        newNd = DSAListNode(value) 
        if self.isEmpty():
            self.head = newNd 
            self.tail = newNd
            # self.setNext(None)
            # self.setPrev(None)
        else:
            
            currNd = self.head
            while currNd.getNext() != None:
                currNd = currNd.getNext() # finding last insert

            currNd.setNext(newNd) 
            newNd.setPrev(self.tail) 
            self.tail = newNd
                  
    def isEmpty(self) -> bool:

        if self.head == None:
            empty = True
        else:
            empty = False
        return empty

    def peekFirst(self):
        if self.isEmpty():
            raise ValueError("List is empty ")
        else:
            nodeValue = self.head.getValue()
        return nodeValue

    def peekLast(self):
        if self.isEmpty():
            raise ValueError("List is empty ")
        else:
            lastNd = self.tail.getValue()
        return lastNd
    
    def removeFirst(self):
        cur = self.head
        if self.isEmpty():
            raise ValueError("List is empty ")

        elif not cur.next: # if there is only one value
            nodeValue = self.head.getValue() #gets the value of the first node
            self.head = None
            
        else: 
            nodeValue = self.head.getValue() #gets the value of the first node
            self.head = self.head.getNext() # points the head to the second node removing the first 
            self.prev = None

        self.count-=1

        return nodeValue

    def removeLast(self):
        if self.isEmpty():
            raise ValueError("List is empty ") 
        elif self.head.getNext() == None:
            nodeValue = self.head.getValue()
            self.head = None
        
        else:
            prevNd= self.tail.prev
            currNd = self.head
            while currNd.getNext() != None:
                prevNd = currNd
                currNd = currNd.getNext()
            prevNd.setNext(None)
            nodeValue = currNd.getValue()
            self.tail = prevNd

        self.count -= 1

        return nodeValue

    def find(self,value):
        node = self.head
        while node != None and value != node.value:
            node = node.next
        return node

    def removeAny(self, value):
        if self.isEmpty():
            raise ValueError("List is empty ")
        value = self.find(value)

        if value is self.head:
            self.head = value.next
        else:
            value.prev.next = value.next

        if value is self.tail:
            self.tail = value.prev
        else:
            value.next.prev = value.prev
        return value.value






    # def displayList(self):
    #     currNd = self.head
    #     l = []
    #     while currNd != None:
    #         l.append(currNd.value) 
    #         currNd = currNd.getNext()
            
    #     print("\nList = ",l)


    

class ListError(Exception):
    pass


ll = DSALinkedList()

ll.insertLast("a")
ll.insertLast("b")
ll.insertLast("c")
ll.insertLast("d")
ll.insertLast("e")

# for i in ll:
#     print(f"{i}")

ll.removeAny("d")

for i in ll:
    print(f"{i}")
# print("head:", ll.head.value)
# print("tail: ",ll.tail.value)
# print("next from head:", ll.head.next.value)
# print("prev from tail:", ll.tail.prev.value)
# ll.removeFirst()
# ll.displayList()
# print("head:", ll.head.value)
# print("tail: ",ll.tail.value)
# print("next from head:", ll.head.next.value)
# print("prev from tail:", ll.tail.prev.value)
# ll.removeLast()
# ll.displayList()
# print("next from head:", ll.head.next.value)
# print("prev from tail:", ll.tail.prev.value)
# print("head:", ll.head.value)
# print("tail: ",ll.tail.value)

# ll.removeLast()
# ll.displayList()
# print("tail: ",ll.tail.value)
# print("head:", ll.head.value)

# ll.insertFirst(1)
# ll.insertFirst(2)
# ll.insertFirst(3)
# ll.insertFirst(4)
# ll.insertLast(5)
# ll.insertLast(9)
# ll.insertFirst(1)


# for i in ll:
#     print(i)

# print("tail:",ll.tail.value)
# print("head:", ll.head.value)
# print("next from head:", ll.head.next.value)
# print("prev from tail:",ll.tail.prev.value)

# print("prev:",ll.tail.prev.value)


# print(ll.__next__())


