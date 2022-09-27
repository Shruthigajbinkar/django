def decfun(fun):
    def innerfun():
        print('*'*20)
        fun()
        print('*'*20)
    return innerfun
@decfun

def display():
    print('iam display')
display()
