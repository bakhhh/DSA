# Sohail Bakhshi 
# Student ID - 20605126
#This code is inspired by the pseudocode from Lecture 2 Pg 33

def wrapperIT(n):
    if type(n) == str:
        raise TypeError("Value entered cant be string ")
    if n < 0:
        raise ValueError("Value entered cant be negative ")
    else: 
        return calcNFactorial(n)

def wrapperRecursive(n):
    if type(n) == str:
        raise TypeError("Value entered cant be string ")
    if n<0:
        raise ValueError("Value cannot be negative")

    return calcNFactorialRecursive(n)

def calcNFactorial(n): #iterative solution
    nFactorial = 1
    for i in range(n, 1, -1):
        nFactorial = nFactorial * i
    return nFactorial

def calcNFactorialRecursive(n): #recursive solution
    if n == 0:
        return 1
    else:
        return n * calcNFactorialRecursive(n-1)
def main():    
    try:
     
        print("Iterative Factorial =", wrapperIT(9))

        print("Recursive Factorial =",wrapperRecursive(5))

    except Exception as e:
        print("Error: ", e)

main()