#normal function declaration

def square(n):
    return n*n

print(square(6))

#recursion

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


print("enter the number")
# print(fact(int(input())))
print(fact(5))

#lambda function - anonymous functions syntax is lambda arguments: expression

bro = lambda x: x*x
print(bro(5))


#tower of hanoi

def hanoi(n,source,destination,auxiliary):
    if n==1:
        print("move disk 1 from source",source,"to destination",destination)
        return
    hanoi(n-1,source,auxiliary,destination)
    print("move disk",n,"from source",source,"to destination",destination)
    hanoi(n-1,auxiliary,destination,source)


hanoi(4,"A","B","C")

#greater of two numbers

a=int(input("enter the first number"))
b=int(input("enter the second number"))
maximum = lambda a,b :a if a>b else b
print(maximum(a,b))

#map function

list1=[]
list2=[]
n=int(input("enter the number of elements in list 1"))

for i in range(0,n):
    ele1=int(input())
    list1.append(ele1)

print(list1)

m=int(input("enter the number of elements in list 2"))

for i in range(0,m):
    ele2=int(input())
    list2.append(ele2)

print(list2)

result=map(lambda x,y:x+y,list1,list2)
print(list(result))

#filter function

arr1=[]
N=int(input("enter the number of elements in list"))
print("enter the elements")
for i in range(0,N):
    ele=int(input())
    arr1.append(ele)
print(arr1)
print("cube of the elements in the list")

arr2=[]
arr2=list(map(lambda x:x*x*x,filter(lambda x:x%2!=0,arr1)))
print(arr2)
