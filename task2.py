class Employee:
    
    def __init__(self,name,id):
        self.name=name
        self.id=id
        

class Manager(Employee):
    developers=[]
    testers=[]
    
    def addDev(self,dev):
        if(self.developers.count(dev.id)==0):
            self.developers.append(dev.id) 
        dev.manager=self.id
        return self
    
    def removeDev(self,dev):
        if(self.developers.count(dev.id)==1):
            self.developers.remove(dev.id)
        dev.manager=None
        return self
    
    def addTest(self,tester):
        if(self.testers.count(tester.id)==0):
            self.testers.append(tester.id)
        tester.manager=self.id
        return self
    
    def removeTest(self,tester):
        if(self.testers.count(tester.id)==1):
            self.testers.remove(tester.id)
        tester.manager=None
        return self

class Developer(Manager):
    pass

class Tester(Manager):
    pass

dev1=Developer('dev1',1)
man1=Manager('man1',3)

man1.addDev(dev1)

print(dev1.manager)