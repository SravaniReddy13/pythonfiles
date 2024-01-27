a=int(input('enter a value:'))
b=int(input('enter b value:'))
c=input('enter arithmetic operator')
match c:
    case '+':
        print(a+b)
    case '-':
        print(a-b)    
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '//':
        print(a//b)
    case '%':
        print(a%b)
    case '**':
        print(a**b)
    case _:
        print('enter valid operator')