file1 = open("file1.txt", "r")
List = list()
for line in file1:
    List.append(line.split())
List.sort()
print(List)

n = 5
List = list()
print("ENTER 5 NUMBERS:")
for i in range(n):
    List.append(int(input("ENTER A NUMBER: ")))

file1 = open("file1.txt", "w")
for val in List:
    file1.write(str(val)+"\n")
file1.close()