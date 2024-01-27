class mtca:
    principalname='Mr.prabhakar naidu'
    collegename='mother theresa institute of computer applications'
    location='palamaner'
    def __init__(self,sname,mobile,email):
        self.studentname=sname
        self.mobileno=mobile
        self.email=email

    def update_mobile(self,new):
        self.mobileno=new
        print('mobile numbers updated')
    @classmethod
    def change_principal(cls,new):
        cls.principal=new
    @staticmethod
    def add(a,b):
        return a+b

sravani=mtca('sravani',48755775758,'jhsdjdh@gmail.come')
sravs=mtca('sravs',7783846778,'ghfjfjfh@gmail.com')

