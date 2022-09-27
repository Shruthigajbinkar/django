#multtiple inheritance

class A:

    def display(self):
        print('iam display from class A')

class B:

     def show(self):
         print('iam show from class B')
         
class C(A,B):
    def info(self):
        print('iam info from class C')

C1=C()
C1.display()
C1.show()
C1.info()
print(C.mro())
