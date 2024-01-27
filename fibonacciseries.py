a=0
b=1
i=1
print(a,b,end=',')
while i<=10:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1