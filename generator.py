#def fun(a,b):
 #   yield a+b
  #  yield a*b
#out=fun(2,3)
#print(list(out))

#def fun(n):
 #   a,b=0,1
  #  for _ in range(n):
   #     yield a
    #    a,b=b,a+b
#print(list(fun(10)))
#def fun(n):
    #a=1
   # for _ in range(n):
  #      yield a
 #       a*=2
#print(list(fun(10)))

def fun(n):
    d=''
    while n>0:
        d+=(
            n%2)
        n//=2
    yield d
b=(list(fun(10)))
i=-1
out=""
while i<-len(b):
    out+=[b[i]]
    i-=1
print(out)


