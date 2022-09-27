x=10

def divide(num):
    res=num/x
    return res

output=divide(20)
print(output)


x=10

def modify():
    global x
    x=0

def divide(num):
    res=num/x
    return res

modify()
output=divide(20)
print(output)
