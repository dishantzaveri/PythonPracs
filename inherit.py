class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

#inheritance 

class Student(Person):
     def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
x=Student("Dishant","Zaveri")
x.printname()

#super


class Student(Person):
     def __init__(self,fname,lname):
        super().__init__(fname,lname)
x=Student("Dishant","Zaveri")
x.printname()