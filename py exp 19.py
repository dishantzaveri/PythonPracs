import re
file1 = open('file1.txt','r')
para = file1.read()
pattern = re.compile("(0|91)?[6-9][0-9]{9}")

for num in para.split():
    if pattern.match(num):
        print(num)