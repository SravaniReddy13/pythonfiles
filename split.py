s=input('enter a string')
i=0
d=[]
temp=' '
while i<len(s):
    if s[i]!=' ':
        temp+=s[i]
    else:
        d+=[temp]
        temp=' '
    i+=1
else:
    if temp:
        d+=[temp]
print(d)
