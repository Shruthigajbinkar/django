import random
li=(1,3,5,7,9)
output=[]
indexes=[]
for i in range(0,100):
    
    idx=random.randint(0,len(li)-1)
    
    if idx not in indexes:
        output.append(li[idx])
        indexes.append(idx)
    if len(li) == len(output):
        break
