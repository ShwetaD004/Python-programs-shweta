#Program of multiple inheriance
class Mother:
    def mget(self,mname,mage):
        self.mname=mname
        self.mage=mage
    def mdisplay(self):
        print("My Mother name is ",self.mname," Her age is ",self.mage)

class Father:
    def fget(self, fname,fage):
        self.fname=fname
        self.fage=fage
    def fdisplay(self):
        print("My Father name is ",self.fname," His age is ",self.fage)

class Son(Mother,Father):
    pass
    

obj=Son()
obj.mget("Sonal",30)
obj.mdisplay()
obj.fget("Jitesh",35)
obj.fdisplay()