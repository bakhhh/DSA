# Sohail Bakhshi 
# Student ID - 20605126
#This code is inspired by the pseudocode from Lecture 2 Pg 58

def moveDisk(n, source, dest, level =1):
    space = '      '
    indnt = level*space # allows indentation for each level
    print(f"{indnt} Recursion Level = {level}")
    print(indnt,"Move disk %i from source %s to destination %s" %(n, source, dest))
    print(f"{indnt} n = {n}, src = {source}, dest = {dest}\n")

def towers(n, start, dest, level =1):
    
    if n == 1: # if we have 1 disk
        moveDisk(n, start, dest,level) #prints out the statements in moveDisk()
    else:
        temp = 6 - start - dest
        towers(n-1, start, temp, level+1)
        moveDisk(n, start, dest, level)
        towers(n-1, temp, dest, level+1)


n,start,dest =3,1,3
towers(int(n), int(start), int(dest))