#amstrong
num= int(input('enter a number:'))
sum=0
temp= num
while num>0:
     digit=num%10
     sum+=digit**3
     num//=10

if num==sum:
    print("num,is an amstrong number")
else:
   print("num,is not an amstrong number")
          
