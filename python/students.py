#students

class Student:

    SCHOOL_NAME='V CUBE'
    def __init__(self,name,age,m1,m2):
        self.name=name
        self.age=age
        self.english_marks=m1
        self.maths_marks=m2

    def info(self):
        print(self.name,self.age,Students.SCHOOL_NAME)

S1=Student('raju',30,40,60)
S1 info()
    
