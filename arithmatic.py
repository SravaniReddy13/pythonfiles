a=int(input('enter a value'))
b=int(input('enter b value'))
c=input('enter any arithmatic operator')
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='//':
    print(a//b)
elif c=='%':
    print(a%b)
elif c=='**':
    print(a**b)
else:
    print('enter valid operator')