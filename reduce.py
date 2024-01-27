from functools import reduce
reduce
a=[1,2,3,4,5]
#print(reduce(lambda x,y:x+y,a))
b=list(map(lambda i:i**2,a))
print(reduce(lambda x,y:x+y,b))
