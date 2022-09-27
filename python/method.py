#method

class First:

    def display(self):
        print('iam display from class First')

obj1=First()
obj1.display()
print(id(obj1))

obj2=First()
obj2.display()
print(id(obj2))
