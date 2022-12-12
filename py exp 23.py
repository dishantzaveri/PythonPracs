# #Python Interitance
class Employee:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname


class Developer(Employee):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


class Tester(Employee):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


class Manager(Developer, Tester):
    employees = []

    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def addDeveloper(self, fname, lname):
        employee = Developer(fname, lname)
        self.employees.append(employee)

    def addTester(self, fname, lname):
        employee = Tester(fname, lname)
        self.employees.append(employee)

    def displayEmployees(self):
        for i in self.employees:
            print(i.firstName, i.lastName)

    def removeDeveloper(self, fname, lname):
        for i in self.employees:
            if i.firstName == fname and i.lastName == lname:
                if type(i) == Developer:
                    self.employees.remove(i)
                    del (i)
                else:
                    print(fname, lname, "is not a developer")

    def removeTester(self, fname, lname):
        for i in self.employees:
            if i.firstName == fname and i.lastName == lname:
                if type(i) == Tester:
                    self.employees.remove(i)
                    del (i)
                else:
                    print(fname, lname, "is not a tester")


m1 = Manager("Manan", "Shah")
m1.addDeveloper("Devraj", "Mishra")
m1.addTester("Yuvraj", "Thakur")
m1.addDeveloper("Heet", "Zatakia")
m1.displayEmployees()
m1.removeDeveloper("Devraj", "Mishra")
m1.removeDeveloper("Yuvraj", "Thakur")
m1.displayEmployees()


class Person:
    def __init__(self, name, age):
        self.name = name
#         self.age = age
#     def __str__(self) :
#         return f"{self.name} ( {self.age})"
# p1=  Person("John", 36)
# print (p1)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 =  Person ( "John", 36)
# print (p1.name)
# print (p1.age)
# del p1.age
# print(p1.age)


# class Person (object):
#     def __init__(self,name):
#         self.name = name

#     def getName(self) :
#         return self.name
#     def isEmployee ( self) :
#         return False
# class Employee ( Person):
#     def isEmployee ( self) :
#         return True
# emp = Person ("p1")
# print (emp.getName(), emp.isEmployee())
# emp = Employee( "p2 ")
# print (emp.getName(), emp.isEmployee() )
