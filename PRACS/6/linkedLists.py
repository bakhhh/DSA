class DSAListNode: #Previously submitted for Practical 4 in COMP1002, Sem 2, 2022
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


    def getCount(self):
        return self.count
        
    def getTail(self):
        return self.tail
    
    def insertFirst(self, value):
        newNd = DSAListNode(value)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            self.head.prev = newNd 
            newNd.next = self.head
            self.head = newNd
        self.count += 1

        
    def insertLast(self, value):
        newNd = DSAListNode(value) 
        if self.isEmpty():
            self.head = newNd 
            self.tail = newNd
        else:
            
            currNd = self.head
            while currNd.getNext() != None:
                currNd = currNd.getNext() # finding last insert

            currNd.setNext(newNd) 
            newNd.setPrev(self.tail) 
            self.tail = newNd
        self.count += 1
                  
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

    def find(self,value): #finds values
        node = self.head
        while node != None and value != node.value:
            node = node.next
        return node


    def removeAny(self, value): #added new function to remove any
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
    

class ListError(Exception):
    pass
