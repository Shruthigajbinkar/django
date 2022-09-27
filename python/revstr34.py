s='cde0fgiuhxae'
vowels='aeiou'
cnst=0
cnt=0
output=' '
for i in range(0,len(s)):
    if s[i] not in vowels:
        cnst=1
    if cnst==1 and s[i] in vowels:
        cnt=cnt+1
        output+=s[i]
    elif cnt>1 and s[i] not in vowels:
        print(output)
        cnt=0
        output=' '
    elif cnt<=1:
        cnt=0
        output=' '

    
    
    
