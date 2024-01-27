def fibonacci(a,b=0,c=1,res=()):
    if c>=a:
        return res
    elif b==0:
        res+=(b,c)
    else:
        res+=(c,)
    return fibonacci(a,c,b+c,res)
print(fibonacci(100))
print(fibonacci(50))