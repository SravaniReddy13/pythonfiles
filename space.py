s="hello my is sravani"
i=0
out=" "
while i<len(s):
    if s[i]==' ':
        out+='_'
    else:
        out+=s[i]
    i+=1
print(out)