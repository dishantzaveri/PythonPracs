## Built in functions

#Type conversion
a = int(5.5)
print("float -> int",a)

b = float(5)
print("int -> float",b)

c = str(10)
print("int -> string",c)

d = int("9")
print("str -> int",d)

#Type coercion

m = 1 + 1.5
print(m)

#Mathematical Functions
import math

s = math.sin(30)
print(s)

#Date and Time
import time

t = time.localtime(time.time())
print(t)

t_new = time.asctime(time.localtime(time.time()))
print(t_new)



import calendar
a = calendar.month(2022,9)
print(a)

#dir() function
import math

list_dir = dir(math)
print(list_dir)

#help() function
import math
math_help = help(math.ceil)

list=dir(math)
print(list)

help(math.log2)

