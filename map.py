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