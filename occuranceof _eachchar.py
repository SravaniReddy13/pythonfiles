s=input('enter a string')
r={}
for char in s:
    if not char in r:
        r[char]=1
    else:
        r[char]+=1
print(r)
