#a='xyz'
#b=[1,2,3]
#out={a[i]:b[i]  for i in range(0,len(a))}
#print(out)

a={'a':'abc',1:1234,'b':'bcdw',2:2354}
out={a[i]:i for i in a  if type(a[i])==str}
print(out)