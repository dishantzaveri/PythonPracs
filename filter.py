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

#reduce function

from functools import reduce
nums=[1,2,3,4,5,6,7,8,9,10]

summ = reduce(lambda a,b:a+b,nums)
print(summ)