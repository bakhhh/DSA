#File: #DSALinkedList.py 
#Name: Sohail Bakhshi 
#Student ID - 20605126
#Unit - Comp1002
#Last modified - 8/4/22
#Data Structures & Algorithms Assignment
#Previously submitted for Practical 4 in COMP1002, Sem 2, 2022

from myException import * #custom exception
#ListNode class used within linked list class
class DSAListNode: 
    def __init__(self, value:object):
        self.value = value
        self.next = None
        self.prev= None

#Method: getValue
#Returns value
    def getValue(self): #returns the value of the node
        return self.value

#Method: setValue
#sets the value of the node
    def setValue(self, inValue): # sets the value of the node
        self.value = inValue

#Method: getNext
#gets the next value in the linked list
    def getNext(self): 
        return self.next   

#Method: getPrev
#gets the previous value in the linked list
    def getPrev(self):  
        return self.prev

#Method: setNext
#sets the next value in the linked list
    def setNext(self, newNext):
        self.next = newNext

#Method: setPrev
#sets the previous value in the linked list
    def setPrev(self, prev): 
        self.prev = prev
    
#Linked List class
class DSALinkedList():
  
    def __init__(self):
        self.head = None # the value at the top of the list
        self.tail = None # the value at the bottom of the list
        self.count = 0

#Method: __iter__
#Allows iteration
    def __iter__(self):   #Lecture 4 slide 72 COMP1002, Sem 2, 2022 #allows me to iterate through the linked list
        curNd = self.head
        while curNd != None:
            yield curNd.value
            curNd = curNd.next

#Method: getCount
#returns count
    def getCount(self): #returns how many items are in the linked list
        return self.count

#Method: getTail
# returns the tail value     
    def getTail(self): 
        return self.tail

#Method: insertFirst
#function that allows me to insert at the very front of the list 
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

#Method: insertLast
# inserts at the end of the list
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

#Method: isEmpty
#checks if the linked list is empty  
    def isEmpty(self): 
        if self.head == None:
            empty = True
        else:
            empty = False
        return empty

#Method: peekFirst
#returns the first value
    def peekFirst(self):
        try:
            if self.isEmpty():
                raise valueError("List is empty ")
            else:
                nodeValue = self.head.getValue()
            return nodeValue
        except valueError as e:
            print(e)

#Method: peekLast
#returns the last value
    def peekLast(self):
        try:
            if self.isEmpty():
                raise valueError("List is empty ")
            else:
                lastNd = self.tail.getValue()
            return lastNd
        except valueError as e:
            print(e)


#Method: removeFirst
#function that removes the first value 
    def removeFirst(self): 
        try:
            cur = self.head
            if self.isEmpty():
                raise valueError("List is empty ")  #checks if list is empty if theres no values then how can it remove anything

            elif not cur.next: # if there is only one value
                nodeValue = self.head.getValue() #gets the value of the first node
                self.head = None
                
            else: 
                nodeValue = self.head.getValue() #gets the value of the first node
                self.head = self.head.getNext() # points the head to the second node removing the first 
                self.prev = None

            self.count-=1 # -1 from count as one less value in the list

            return nodeValue
        except valueError as e:
                print(e)


#Method: removeLast
#function that removes the last value 
    def removeLast(self): 
        try:
            if self.isEmpty():
                raise valueError("List is empty ")  #checks if list is empty if theres no values then how can it remove anything
            elif self.head.getNext() == None: # checks if the first value is the only value
                nodeValue = self.head.getValue()
                self.head = None       
            else:
                prevNd= self.tail.prev 
                currNd = self.head
                while currNd.getNext() != None: #finds the last value
                    prevNd = currNd
                    currNd = currNd.getNext()
                prevNd.setNext(None) #sets the previous node to point at null
                nodeValue = currNd.getValue()
                self.tail = prevNd

            self.count -= 1 # -1 from count as one less value in the list

            return nodeValue
        except valueError as e:
            print(e)

        
#Method: find
#finds values inputed  #function added to support with removing any
    def find(self,value): 
        currNd = self.head 
        while currNd != None and value != currNd.value: #searches through the linked list until found the value
            currNd = currNd.next
        return currNd #returns the node

#Method: find
#returns boolean if found 
    def checkFind(self,value): 
        found= True
        if not self.find(value):
                found = False
        return found

#Method: removeAny
#added new function to remove any value in the list
    def removeAny(self, value):
        try:
            if self.isEmpty():
                raise valueError("List is empty ") #check if empty
            value = self.find(value) #uses the find function to find the value that is going to be removed
            if value == self.head:  
                self.head = value.next #if the value is the head value then the next value is now the head
            else:
                value.prev.next = value.next #if the value is in the middle of the list it gets the previous value and points it to the next value 
            if value == self.tail:
                self.tail = value.prev #if value is the tail point the previous node to tail
            else:
                value.next.prev = value.prev  #if the value is in the middle of the list it gets the previous value and points it to the next value 
            return value.value
        except valueError as e:
            print(e)


#Method: replaceNode
#replaces node with new node 
# was originally meant to be used for updating vertices in the graph but it creating problems
    def replaceNode(self,old, new): 
        try:
            if self.checkFind(old) == False:
                raise valueError(f"\n{old} not found ")
            else:
                currNd = self.find(old) #finds the old node 
                newNd = DSAListNode(new)  #creates new node
                if currNd.value == old:
                    currNd.value = newNd.value #sets the old node to new node
        except valueError as e:
            print(e)


        
