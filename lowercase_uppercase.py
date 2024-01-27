a=input('enter a string')
i=0
d=" "
while i<len(a):
    if 'a'<=(a)<='z':
     d+=chr(ord(a[i])-32)
    else:
       d+=a[i]
    i+=1
print(d)