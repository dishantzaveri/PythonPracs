#Python program to print each line of a file in reverse order.
file1=open("file1.txt","r")
# file2=open("reversedata.txt","w")
# data=file1.read()
# revdata=data[::-1]
# file2.write(revdata)
data = file1.readlines()
for line in data:
    print(line[::-1])
file1.close()
