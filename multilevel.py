class A:
    def __init__(self,c,d):
        self.c=c
        self.d=d


class B(A):
    def __init__(self,c,d,e,f):
        super().__init__(c,d)
        self.e=e
        self.f=f

class c(B):
    def __init__(self,c,d,e,f,g,h):
        super().__init__(c,d,e,f)
        self.g=g
        self.h=h
obj=c(2,3,4,5,6,7)       

