#. Python program to compute the number of characters, words and lines in a file
file1=open("file1.txt","r")
num_of_char=0
num_of_words=0
num_of_lines=0
num_of_spaces=0

# for line in file1:
#     num_of_lines+=1
#     word='Y'
#     for letter in line:
#         if(letter!=' ' and word=="Y"):
#             num_of_words+=1
#             word='N'
#         elif letter==" ":
#             num_of_spaces+=1
#             word="Y"
#         for i in letter:
#             if(i!=" " and i!="\n"):
#                 num_of_char+=1
                    
# print(num_of_char)
# print(num_of_lines)
# print(num_of_words)

data = file1.readlines()
for line in data:
    num_of_char+=len(line)
    num_of_lines+=1
    num_of_words+=len(line.split())

print("Number of characters in file : ",num_of_char)
print("Number of words in file : ",num_of_words)
print("Number of lines in file : ",num_of_lines)

file1.close()