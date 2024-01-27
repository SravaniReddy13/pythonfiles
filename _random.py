import random
number=random.randint(100,1000)
while True:
    a=int(input('ente a number'))
    if a==number:
        print('congrats you successfully gused the number')
    elif a<number:
        print('enter some greatest number')
    else:
        print('enter some lesser number')