a=[9,'9',10,[1,3],'234',21,22.5]
out=[(i,a[i]) for i in range(0,len(a)) if type(a[i])==int]
print(out)