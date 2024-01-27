per1=input('enter any vlaue')
per2=input('enter any value')
if per1=='rock' and per2=='paper':
    print('per1 is winner')
elif per1=='paper' and per2=='scissor':
    print('per2 is winner')
elif per1=='rock' and per2=='scissor':
    print('per1 is winner')
elif per1==per2:
    print('match tie')
else:
    print('try again')