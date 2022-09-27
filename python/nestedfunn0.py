#nested function

def outerfun():
    print('iam outerfun')

    def innerfun():
        print('iam innerfun')

        innerfun()
        return

fun=outerfun()
innerfun()
fun()
          
