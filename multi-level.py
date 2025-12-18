class father :
    surname="singh"
class son(father) :
    def show(self):
        print("akash", self.surname)
class gson (son):
    def disp(self):
        print("ankit",self.surname)
s=son()
s.show()

gs=gson()
gs.disp()
gs.show()
