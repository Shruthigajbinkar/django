#class

class First:

    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def show(self):
        print(self.num1,self.num2)
    def display(self):
        print('iam display from class First')
obj1=First(10,20)
obj1.show()
