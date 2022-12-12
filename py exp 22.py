# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]

# l3 = list(map(lambda x,y: x+y, l1,l2))
# print(l3)

a = [i for i in range(1,11)]
a1= filter(lambda x:x%2!=0,a)
a2 = map(lambda x:x**3, a1)
a3 = list(a2)
print(a3)
