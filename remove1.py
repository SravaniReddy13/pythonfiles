s=input('enter any string')
i=''
for char in s:
    if char not in i:
        i+=char
print(i)