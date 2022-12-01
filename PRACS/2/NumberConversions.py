# Sohail Bakhshi 
# Student ID - 20605126
#Code for Number Conversions allowing you to convert from decimal to the selected base
#References:
# Bparanj. 2020. "Generic Decimal to Any Base Conversion using Recursion." https://www.youtube.com/watch?v=szkJP9bSr3k

def wrapperConv(n, base):
    if n < 0:
        raise ValueError("Value entered cant be negative ")
    if base < 0:
        raise ValueError("Base value entered cant be negative ")
    
    else: 
        return conversions(n,base)


def conversions(n, base):
   
    if n < base:  #if n is less than base return n
        return n 
    else:
        return 10 * conversions(n//base, base) + (n%base) #otherwise call function 


def main():
    try:
        num = int(input("Enter a number: "))
        base = int(input("Enter a base (2-16): "))
        print(wrapperConv(num, base))
        
    except Exception as e:
        print("Error", e)
    
    
    
main()

