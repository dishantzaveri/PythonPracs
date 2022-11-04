class Employee:    

    def __init__(self, id, name, salary, designation):  

        self.id = id        

        self.name = name  

        self.salary = salary        

        self.designation = designation  

 

class Developer(Employee):  

    pass  

 

class Tester(Employee):  

    pass  

class Manager(Employee):  

    listDevelopers = []    

    listTesters = []      

    def addDeveloper(self, id, name, salary):          

        d = Developer(id, name, salary, "Developer")        

        self.listDevelopers.append(d)  

 

    def removeDeveloper(self, id):        

        for developer in self.listDevelopers:            

            if(developer.id == id):  

                self.listDevelopers.remove(developer)  

 

    def addTester(self, id, name, salary):        

        t = Developer(id, name, salary, "Tester")        

        self.listTesters.append(t)  

 

    def removeTester(self, id):        

        for tester in self.listTesters:            

            if(tester.id == id):  

                self.listTesters.remove(tester)    

    def showEmployees(self):        

        print("Developers:")        

        for developer in self.listDevelopers:  

            print(developer.name)        

        print("Testers:")        

        for tester in self.listTesters:            

            print(tester.name)  


m1 = Manager(1, "ABC", 100000, "Manager")

m1.addDeveloper(2, "DEF", 50000)

m1.addDeveloper(3, "GHI", 45000)

m1.addDeveloper(4, "JKL", 40000)

m1.addTester(5, "MNO", 20000)

m1.addTester(6, "PQR", 20000)

m1.showEmployees()

m1.removeDeveloper(3)

m1.removeTester(6)

m1.showEmployees()