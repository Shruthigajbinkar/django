#scope

x=10
def display():
    
    x=30
    
    print(x)
    
    display()
    
    print(x)
def display():
    global x
    x=20
    print(x)
    display()
    print(x)
