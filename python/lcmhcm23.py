num1=int(input('enter a number:'))
num2=int(input('enter another number:'))
div=2
while div<=num1:
    if num1%div==0 and num2%div==0:
        print(div)
        break
