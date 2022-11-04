#greater of two numbers

a=int(input("enter the first number"))
b=int(input("enter the second number"))
maximum = lambda a,b :a if a>b else b
print(maximum(a,b))
