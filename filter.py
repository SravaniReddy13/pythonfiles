b=[1,0,True,'','str',[1,2,3],78,0.0]
out=[i for i in b if bool(i)]
print(out)

a=[2,4,3,23,2,1,21,35,8,9]
def multiple3(num):
    if num%3==0:
        return True
    else:
        return False
print(list(filter(multiple3,a)))
print(list(filter(lambda num:num%3==0,a)))
