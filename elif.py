a=input('enter any character')
if a in '0123456789':
    print('it is a number')
elif a in 'A'<=a<='Z':
    print('it is a uppercase letter')
elif a in 'a'<=a<='z':
    print("it is a lowercase letter")
else:
    print('it is a special character')