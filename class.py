class Dishu:
    a=10
p1=Dishu()
print(p1.a)

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
# p1=Person("Devraj","Mishra")
# print(p1.firstname)
# print(p1.lastname)
    def printname(self):
        print(self.firstname,self.lastname)

p1=Person("Devraj","Mishra")
p1.firstname=("scam")
p1.printname()

fn=input("enter fname")
ln=input("enter lname")
p1=Person(fn,ln)
p1.printname()

print(p1)
del p1
print(p1)

