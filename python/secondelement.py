num=int(input('enter a number:'))
s=0
while num>0:
    t=num%10
    s=s+t
    num=num//10
    print(s)
