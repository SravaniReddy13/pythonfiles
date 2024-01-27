def fun(a,b):
    if len(a)==len(b):
        i=0
        c=0
        while i<len(a):
            if not a[i]==b[i]:
                c+=1
            i+=1
    else:
        print('enter proper inputs')
    return c
print(fun('string','strong'))             