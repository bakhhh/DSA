# Sohail Bakhshi 
# Student ID - 20605126
#This code is inspired by the pseudocode from Lecture 2 Pg 41 and 43


def wrapperIT(n):
    if type(n) == str:
        raise TypeError("Value entered cant be string ")
    elif n < 0:
        raise ValueError("Value entered cant be negative ")
    else: 
        return fibIterative(n)

def wrapperRecursive(n):

    if type(n) == str:
        raise TypeError("Value entered cant be string ")
    elif n<0:
        raise ValueError("Value cannot be negative")

    return fibRecursive(n)


def fibIterative(n):
    fibVal, currVal, lastVal = 0,1,0

    if n == 0:
        fibVal = 0
    elif n == 1: 
        fibVal = 1
    else:
        for i in range(1,n):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
        
    return fibVal

def fibRecursive(n):
    fibVal = 0
    if n ==0:
        fibVal = 0
    elif n ==1:
        fibVal =1
    else:
        fibVal = fibRecursive(n-1) + fibRecursive(n-2)
    return fibVal


def main():    
    try:

        print("Iterative Fibonacci =", wrapperIT(-1))
  
        print("Recursive Fibonacci =", wrapperRecursive(2))
        

     
    except Exception as e:
        print("Error: ", e)



main()