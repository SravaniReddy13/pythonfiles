def s(li):
    out=[]
    for i in li:
        if type(i) in [str,list,tuple,set,dict]:
            for j in i:
                out+=[j]
    return out
print(s(['abcd',[1,2,3]]))


