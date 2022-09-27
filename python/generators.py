#GENERATORS

def genExp():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')
    yield 3

for i in genExp():
    print('inside for loop')
    print(i)
