a=input('enter a string')
i=0
d=[]
while i<len(a):
    if a[i] in 'aeiouAEIOU':
        d=d+[i]
    i+=1
print(d)