#calculator

class Calc:

    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def addition(self):
        return self.num1+self.num2
C1=Calc(10,20)
res=C1.addition()
print(res)

class NewCalc(Calc):
    def substraction(self):
        return self.num2-self.num1
N1=NewCalc(30,40)
res=N1.substraction()
print(res)
res=N1.addition()
print(res)
