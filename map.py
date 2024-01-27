a=[2,4,5,7,6,8,9]
#print(list(map (lambda i:i**2,a)))
b=list(filter(lambda i:i%2==0,a))
print(list(map(lambda i:i**3,b)))