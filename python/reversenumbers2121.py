#reverse number
num=int(input('enter a number'))
rev=0
while(num>0):
    t=num%10
    rev=rev*10+t
    num=num//10
    print(t,end=' ')
