# Exception understanding






# # 6 name error
# Names = ['Vijay','Dishant','Rohan']
# name.lower()

# # 7 Attribute error
# n=None
# a=n/2

# # 8 TYpeerror
# names = ['Vijay','Dishant','Rohan']
# names/2

# # 9 StopIteration
# list_data = iter([1, 2, 3, 4])
# print(next(list_data))
# print(next(list_data))
# print(next(list_data))
# print(next(list_data))
# print(next(list_data))

# # 10 SyntaxError
# a = 10
# b = 20
# if a>b
#     print("a is large")

# # 11 Exception handling
# try:
#     a,b = eval(input("Enter 2 nos seperated bt comma"))
#     result = a/b
#     print("Result is:",result)
#     if(a==0):
#         raise RuntimeError()
# except ZeroDivisionError:
#     print("Division by zero.")
# except SyntaxError:
#     print("Comma Missing.")
# except RuntimeError:
#     print("Maybe Meaningless.")
# except:
#     print("Somwthing wrong in the input")
# else:
#     print("No exceptions")
# finally:
#     print("Finally call is evaluated.")

# User-defined exceptions




value error

List = [1,2,3,4,5]
a,b,c = List
print(a)
print(b)
print(c)

#arithmetic error

number  = 6
ZeroErro = 6 / 0

#import error

import xyz

list_data = [1, 2, 3, 4, 5]
x=  list_data[6]

index error exception
list_data = [1, 2, 3, 4, 5]
x=  list_data[6]

key error
dict_data={'2' : 'two', '4' : 'four', '6' : 'six'}
dict_data['5']

# keyboard interrupt error
name=input('Enter your name')

#user defined exception


class BaseError(Exception):
    pass
class HighValueError(Exception):
    pass
class LowValueError(Exception):
    pass
value = 29
while(1):
    try:
        n=int(input("Enter number:"))
        if n> value:
            raise HighValueError
        elif n < value:
            raise LowValueError
    except LowValueError:
        print("Very Low Value, Give input again")
        print()
    except HighValueError:
        print("Very High value , give input again")
        print()
    else:
        print("Nice!Correct answer")
        break
