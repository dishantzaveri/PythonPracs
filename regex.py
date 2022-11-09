import re
file = open('sample.txt','r')
text = file.read()

pattern =  r'[a-zA-Z0-9\.\-+=]+@[a-zA-Z0-9\-+=]+\.[a-zA-Z0-9\.\-+=]+'
emails= re.findall(pattern,text)
print(emails)

# pattern = r'M\w*\.\s*\w*\s*\w*'

# u=re.findall(r'\S+.@',text)
# d=re.findall(r'@\S+.',text)
# for i,j in zip(u,d):
#     print("userid:",i[:-1],"domain:",j[1:])

# print(u)
# print(d)

# website=r'\b(https?://)?(www/plus)[.][a-zA-Z0-9\.\-+=]+\.[a-zA-Z0-9\.\-+=]+'

# u=re.findall(website,text)
# d=re.findall(r'@\S+.',text)
# for i,j in zip(u,d):
#     print("userid:",i[:-1],"domain:",j[1:])

# print(u)
# print(d)
