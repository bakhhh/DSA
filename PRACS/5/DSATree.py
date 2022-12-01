
from DSAQueue import * #Previously submitted for Practical 3 in COMP1002, Sem 2, 2022

class TreeNode:
    def __init__(self,key,value: object):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return (f"Key: {str(self.key)} Value: {str(self.value)}")
    
    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left

    def setLeft(self, newLeft):
        self.left = newLeft

    def getRight(self):
        return self.right
    
    def setRight(self,newRight):
        self.right = newRight


class BinarySearchTree(TreeNode):
    def __init__(self):
        self.root = None
        self.count = 0
   
    def findRec(self, key, curNode:TreeNode):
        try:
            if curNode is None:
                raise ValueError(f"Key {key} not found")
            elif key == curNode.key:
                return curNode.getValue()
            elif key < curNode.key:
                curNode.value = self.findRec(key, curNode.getLeft())
            else:
                curNode.value = self.findRec(key, curNode.getRight())
            return curNode.value 
        except Exception as e:
            print("Error: ", e)

    def find(self,key):
        return self.findRec(key,self.root)
       

    def insert(self, key, value):
        if self.root is None:
            newNd = TreeNode(key, value)
            self.root = newNd
            self.count += 1
        else:
            returnval = self.insertRec(key, value, self.root)
            self.count += 1
            return returnval
        

    def insertRec(self,key,data,curNode :TreeNode):
        try:
            if curNode is None:
                newNd = TreeNode(key, data)
                curNode = newNd
            elif curNode.key == key:
                raise ValueError(f"{curNode.key} is already in the tree")
            elif key < curNode.key:
                left = self.insertRec(key, data, curNode.getLeft())
                curNode.setLeft(left)   
            else: 
                right = self.insertRec(key, data, curNode.getRight())
                curNode.setRight(right)
   
            return curNode
        
        except Exception as e:
            print("Error:", e)


    def delete(self, key):
        self.root = self.deleteRec(key,self.root)
        self.count -=1
        return self.root


    def deleteRec(self, key, curNode:TreeNode):
        update = curNode
        try:
            if curNode is None:
                raise ValueError(f"{key} is not inside the tree")
            elif key == curNode.getKey():
                update = self.deleteNode(key,curNode)
            elif key < curNode.getKey():
                curNode.setLeft(self.deleteRec(key, curNode.getLeft()))
            else:
                curNode.setRight(self.deleteRec(key, curNode.getRight()))
            return update
        except Exception as e:
            print("Error: ", e)

    def deleteNode(self,key,delNode:TreeNode):
        updateNode = None

        if delNode.getLeft() == None and delNode.getRight() == None:
            updateNode = None
        elif delNode.getLeft() is not None and delNode.getRight() == None:
            updateNode = delNode.getLeft()
        elif  delNode.getLeft() == None and delNode.getRight() is not None:
            updateNode = delNode.getRight()
        else:
            def promoteSuccessor(curNode):
                successor = curNode
                if curNode.getLeft() is not None:
                    successor = promoteSuccessor(curNode.getLeft())
                    if successor == curNode.getLeft():
                        curNode.setLeft(successor.getRight())
                return successor
            updateNode = promoteSuccessor(delNode.getRight())
            if updateNode is not delNode.getRight():
                updateNode.setRight(delNode.getRight())
            updateNode.setLeft(delNode.getLeft())

        return updateNode

    def _height(self):
        return self.heightRec(self.root) 
     
    def heightRec(self, curNode:TreeNode):
        if curNode is None:
            height = -1
        else:
            left = self.heightRec(curNode.left)
            right = self.heightRec(curNode.right)
            if left > right:
                height = left +1 
            else:
                height = right +1
        return height

    def min(self):
        return self.minRec(self.root)

    def minRec(self, curNode : TreeNode):
        if curNode.getLeft() is not None:
            minKey = self.minRec(curNode.getLeft())
        else:
            minKey = curNode.key

        return minKey


    def max(self):
        return self.maxRec(self.root)

    def maxRec(self,curNode:TreeNode):
        if curNode.getRight() is not None:
            maxKey = self.maxRec(curNode.getRight())
        else:
            maxKey = curNode.key

        return maxKey

    def balance(self):
        left = self.heightRec(self.root.left)
        right = self.heightRec(self.root.right)
        root = self.heightRec(self.root)
        try:
            if abs(left / right) ==1:
                return 100 #balanced
            else:
                return 100 - abs(left - right)/root *100 #not balanced + showing the percentage balanced
        except ZeroDivisionError:
            return 100 - abs(left - right)/root *100 #not balanced

    def inorder(self): #left -> root -> right
        return self.inorderRec(self.root)

    def inorderRec(self, curNode:TreeNode):
        queue = CircularQueue(self.count)
        def helper(node): # implemented and adjusted based off https://www.youtube.com/watch?v=znTJFkTF-G4
            if not node:
                return
            helper(node.left)
            queue.enqueue(node.key)
            helper(node.right)
        helper(curNode)
        for i in queue:
            return i

    def preOrder(self): #(root, left, right)
        return self.preOrderRec(self.root)

    def preOrderRec(self,curNode):
        queue = CircularQueue(self.count)
        def helper(node):
            if not node:
                return
            queue.enqueue(node.key)
            helper(node.left)
            helper(node.right)
        helper(curNode)
        for i in queue:
            return i

    def postOrder(self): #(left, right, foot)
        return self.postOrderRec(self.root)

    def postOrderRec(self,curNode):
        queue = CircularQueue(self.count)
        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            queue.enqueue(node.key)
        helper(curNode)
        for i in queue:
            return i

    

    

####Testing####          

tree = BinarySearchTree()



def readFile(): #reading in the file
    with open('6degrees.csv','r') as file:
        content =file.readlines()[1:]
        for line in content:
            tree.insert((line.split(',')[0]),(line.split(',')[3])) #inserting movies, name and role
readFile()

tree.find('This is Spinal Tap')
            # self.tree.insert(line.split(',')[0]) #inserting movies, name and role
# tree.insert(10, "ten")
# tree.insert(25, "twenty five")
# tree.insert(61, "sixtyone")
# tree.insert(99, "nintynine")
# tree.insert(103, "hundredandthree")
# tree.insert(1, "sixty")
# tree.insert(14, "fourteen")
# tree.insert(77, "seventy seven")
# tree.insert(6, "six")
# tree.insert(3, "three")
# tree.insert(7, "seven")
# tree.insert(60, "sixty")
# tree.insert(100, "hundred")
# tree.insert(27, "twenty seven")
# tree.insert(8, "eight")
# # tree.insert(27, "twenty seven")
# # tree.insert(14, "fourteen")
# # tree.insert(35, "twenty seven")
# # tree.insert(10, "ten")
# # tree.insert(19, "nineteen")
# # tree.insert(31, "thirtyond")
# # tree.insert(42, "fortytwo")


# print(tree.min())
# print(tree.max())
# print(tree._height())
# print(f"{tree.balance()}%")

# print("Inorder:" ,tree.inorder())

# tree.delete(10)
# tree.delete(25)
# tree.delete(61)
# tree.delete(99)
# tree.delete(103)

# print("Inorder:" ,tree.inorder())
# print("Preorder:" ,tree.preOrder())
# print("PostOrder:" ,tree.postOrder())
# print(f"{tree.balance()}%")
