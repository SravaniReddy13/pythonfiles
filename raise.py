class mobileError(Exception):
    pass
number=int(input('enter a number:-'))
if len(str(number))!=10:
    raise mobileError(f'number should be more than 10 digits but {len(str(number))} were given')
else:
    print('number is validated')