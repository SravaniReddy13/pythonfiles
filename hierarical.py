class mtit:
    chairman='mr.sunil'
    location='palamaner'
    college='mtit'

    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class MCA(mtit):
    principal='Mr.prabhakar naidu'
    strength=250
    staff=10
class Btech(mtit):
    principal='Ms.sravani'
    strength=1500
    staff=50
navya=MCA('navyasree',9867486848)
reva=Btech('reva',67535737683)