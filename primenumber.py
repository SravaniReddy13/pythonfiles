a=int(input('enter any nummber'))
i=1
count=0
while i<=a:
    if a%i==0:
        count+=1
    i+=1
if count==2:
    print('prime number')
else:
    print('not a prime number')