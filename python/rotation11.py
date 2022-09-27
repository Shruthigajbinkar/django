#right rotation
li=[1,2,3,4,5]
output=[]
num=int(input('enter a number:'))
if num in li:
    idx=li.idx(num)
output.extend(li[idx+1:])
output.extend(li[:1+idx])
