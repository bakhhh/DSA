import unittest


class hashTable:
    def __init__(self) -> None:
        self.hashTable={}

    def get(self,key):
        returnVal =self.hashTable.get(key)
        return returnVal

    def put(self,key,value):
        self.hashTable[key] = value

    def remove(self,key):
        self.hashTable.pop(key)





# # # #TESTING
class testhash(unittest.TestCase):

    def testhash(self):
        hasht =hashTable()
        hasht.put('Jake',1)
        hasht.put('Bob',2)
        hasht.put('Billy',3)
        hasht.put('Sam',4)
        hasht.put('Liam',53)
        hasht.put('Kane',6)
        hasht.put('Jack',10)
        hasht.remove('Jack')
        self.assertEqual(hasht.get('Jake'),1)
        self.assertEqual(hasht.get('Bob'),2)
        # print(hasht.hashTable)


 
if __name__ == "__main__":
    unittest.main()