class add:
    @staticmethod
    def add2(a,b):
        return a+b
    @staticmethod
    def add3(a,b,c):
        return a+b+c
class sub:
    @staticmethod
    def sub2(a,b):
        return a-b
class mul:
    @staticmethod
    def mul2(a,b):
        return a*b
class cal(add,sub,mul):
    pass
obj=cal()
print(obj.add2(2,3))
print(obj.add3(2,3,4))
print(obj.sub2(5,3))
print(obj.mul2(2,3))

