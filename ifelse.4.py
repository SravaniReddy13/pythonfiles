a=input('enter any collection')
if len(a)%2==1:
    print(a[len(a)//2])
else:
    print(a[0],a[len(a)-1]) 