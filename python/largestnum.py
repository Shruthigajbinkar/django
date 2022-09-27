li=[10,30,3,15,20]
def maxvalue(list1):
    big = list1[0]
    for val in list1:
        if big<val:
            big=val
        return big
def findindex(list1,val):
    for i in range(0,len(list1)):
        if val==list1[i]:
            return i
        return -1
    for i in range(0,len(li)):
        max_value=maxvalue(li[1:])
        idx=findindex(li,max_val)
        li[i],li[idx]=li[idx],li[i]
print(li)
print(li[1])
        
