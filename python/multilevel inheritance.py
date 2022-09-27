#multilevel inheritance

class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Employe(Person):
    def __init__(self,name,age,empno,salary):
        super().__init__(name,age)
        self.empno=empno
        self.salary=salary
    def eInfo(self):
        print(self.empno,self.salary)
class Manager(Employe):
    def __init__(self,name,age,empno,salary,rights):
        super().__init__(name,age,empno,salary)
        self.rights=rights
    def mInfo(self):
        print(self.rights)
P1=Person('raju',34)
P1.info()
e1=Employe('siva',30,1,100000)
e1.info()
e1.eInfo()
m1=Manager('sri',32,2,20000,'special')
m1.info()
m1.eInfo()
m1=mInfo()
        
