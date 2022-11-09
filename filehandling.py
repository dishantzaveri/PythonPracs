# print("Enter 10 numbers")
# List_input = list()

# fileWrite = open("file1.txt", "w")


# for i in range(10):
#     List_input.append(int(input("Enter number : ")))
#     fileWrite.write(str(List_input[i]))
#     fileWrite.write("\n")

# fileWrite.close()

# #read from the file
# fileRead = open("file1.txt", "r")

# List = list()

# print(fileRead)
# for line in fileRead:
#     List.append(int(line))

# List.sort()
# print(List)
# fileWrite1 = open("file2.txt", "w")

# for i in range(len(List)):
#     fileWrite1.write(str(List[i]))
#     fileWrite1.write("\n")

# fileRead = open("file1.txt", "r")
# List = list()

# f = fileRead.read()
# f = f.split(" ")

# for line in f:
#     List.append(str(line))
# List.sort()
# print(List)
   
# fileWrite = open("file2.txt", "w")

# for i in range(len(List)):
#     fileWrite.write(str(List[i]))
#     fileWrite.write("\n")

# Reverse word


fileRead = open("file1.txt", "r")
List = list()

f = fileRead.read()
f = f.split(" ")

for line in f:
    List.append(str(line[::-1]))
       

fileWrite = open("file2.txt", "w")

for i in range(len(List)):
    fileWrite.write(str(List[i]))
    fileWrite.write("\n")
