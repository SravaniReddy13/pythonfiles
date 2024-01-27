def reverse_vowels(a):
    temp=' '
    for i in a:
        if i in 'aeiouAEIOU':
            temp+=i
    j=-1
    out=' '
    for k in a:
        if k in 'aeiouAEIOU':
            out+=temp[j]
            j+=-1
        else:
            out+=k
    return out
print(reverse_vowels('hello'))
