a=input('enter any string')
i=0
d=" "
temp=True
while i<len(a):
    if a[i]==' ':
        temp=True
    elif temp and 'a'<=a[i]<='z':
        d+=chr(ord(a[i])-32)
        temp=False
    else:
        d+=a[i]
        temp=False
    i+=1
print(d)