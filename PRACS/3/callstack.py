# Sohail Bakhshi 
# Student ID - 20605126
from DSAStack import DSAStack

class callStack(DSAStack):
    def __init__(self, DEFAULT_CAPACITY):
        super().__init__(DEFAULT_CAPACITY)

    def call(self,n,name):
        self.push(f'Method: {name} {str(n)}')
        print("\n############ Adding to stack #############\n")
        self.display()

    def calcNFactorialRec(self, n, fact =1): #recursive solution #from prac2
        self.call(n,'FactorialRecursive')
        if n == 0:
            fact =1
        else:
            fact = n * self.calcNFactorialRec(n-1)
        print("\nPopping: ", self.pop())
        print("count: ", self.count)
        return fact 

    def wrapperRec(self,n): #from prac2
        if type(n) == str:
            raise TypeError("Value entered cant be string ")
        if n<0:
            raise ValueError("Value cannot be negative")

        return self.calcNFactorialRec(n)

def main():
        try:
            stack = callStack(10)
            print("\nRecursive Factorial =",stack.wrapperRec(5))

        except Exception as e:
                print("Error: ", e)

main()
