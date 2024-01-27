def fact(a,i=2):
    if a==i:
        return 'prime'
    elif a%i==0:
        return 'not a prime'
    return fact(a,i+1)
print(fact(1))

    