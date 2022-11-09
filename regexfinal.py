# import re
# file=open('sample.txt','r')
# text=file.read()
# pattern=r'M\w*\.\s*\w*'
# names=re.findall(pattern,text)
# print(names)

# import re
# file=open('sample.txt','r')
# text=file.read()
# pattern=r'[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+'
# emails = re.findall(pattern,text)
# print(emails)

# import re
# file=open('sample.txt','r')
# text=file.read()
# u = re.findall(r'\S+.@',text)
# d = re.findall(r'@\S+.',text)
# for i,j in zip(u,d):
#     print("userid: ",i[:-1],"\nDomain is: ",j[1:])

# website = r'(https?[:]//?(www/plus)[.][a-zA-Z0-9]+([.]com[.]ac/[.]co[.]in\b'
# import re
# file=open('sample.txt','r')
# text=file.read()
# website = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
# result = re.findall(website, text)
# print(result)

import re
file=open('sample.txt','r')
text=file.read()
pattern=r'\d{1,5}.\d{1,3}.\d{1,5}'
phone=re.findall(pattern,text)
print(phone)

