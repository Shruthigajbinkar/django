s=('python','apple','ink')
k=int(input('enter a length you want:'))
for val in s:
    if k<=len(val):
        print(val)
    

li=[1,2,1,1,3,2,4,]
output=[]
count=0
for i in li:
    output[i]=li.count(i)
    print(output)
