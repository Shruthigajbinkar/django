#recursion

i=1

def numbers():
    global i
    print(i)

    if i==1000:
        return
    i=i+1
    numbers()


numbers()
    
