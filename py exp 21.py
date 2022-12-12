#Implement a recursive function to solve tower of Hanoi Problem. Implement lambda function to find greater of the 2 input numbers
def toh(n,source,aux,dest):
    if n==1:
        print("Move disk 1 from source",source,"to destination",dest)
        return
    toh(n-1,source,dest,aux)
    print("Move disk",n,"from source",source,"to destination",dest)
    toh(n-1,aux,source,dest)
n=int(input("Enter number of disks: "))
toh(n,'A','B','C')

max = lambda a,b: max(a,b)
print(max(30,20))
