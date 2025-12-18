class A:
    num1=int(input("enter num1"))
    num2=int(input("enter num2"))
    def add(self):
        print("additon =",self.num1+self.num2)
    def sub(self):
        print("sub =",self.num1-self.num2)
class B(A):
    def multi(self):
        print("multi =",self.num1*self.num2)
    def div(self):
        print("div =",self.num1/self.num2)


ob=B()
ob.multi()
ob.div()
ob.sub()