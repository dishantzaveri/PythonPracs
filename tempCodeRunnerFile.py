try:
    11/0
except ArithmeticError as e:
    print(e)
    print("This is an example of catching ArithmeticError.")