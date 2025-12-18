class father:
    surname="khan"
    def show(self):
        print("my surname is ",self.surname)
class son(father) :
    def disp(self):
        print("my name is ayan ",self.surname)
class son2(father) :
    def out(self):
        print("my name is zaid ",self.surname)

s1=son()
s2=son2()
s1.disp()
s2.out()

s1.show()
s2.show()