# Sohail Bakhshi 
# Student ID - 20605126
#Python Code for Greatest Common Denominator
#References:
# (gcd() in Python - GeeksforGeeks, 2022) https://www.geeksforgeeks.org/gcd-in-python/  
def wrapperCom(x, y):
    if x < 0:
        raise ValueError("Value entered cant be negative ")
    if y < 0:
        raise ValueError("Value entered cant be negative ")
    
    else: 
        return commonDen(x,y)



def commonDen(x, y): 
    if(y==0): #if y = 0 then return x
        return x
    else: # else returns, and checks what number divides by the entered number
        return commonDen(y,x%y)   #calling back the function 

def main():
    try:
        num1= int(input("Enter the first number : "))
        num2= int(input("Enter the second number : "))
        print("The Greatest Common Denominator of %i and %i is:" %(num1, num2), wrapperCom(num1,num2))

    except Exception as e:
        print("Error: ", e)

main()


