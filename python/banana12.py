s=input('enter')
res=[s[i: j] for i in range (len(s)) for j in range(i+1,len(s),+1)]
v=['A','E','I','O','U']
kelvin=0
stuart=0
for i in res:
    if i(0) in v:
        kelvin+=1
    else:
        stuart+=1
if kelvin==stuart:
    print('draw')
elif stuart>kelvin:
    print("stuart"+" "+s(stuart))
else:
    print("kelvin"+" "+s(kelvin))
    
