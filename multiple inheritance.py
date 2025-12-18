class akhiles:
    back="oracle DB & java"
    def backend(self):
        print("backend task  implemnet using",self.back)

class ankush:
    front=" html css & js"
    def frontend(self):
        print("frontend task  implemnet using",self.front)

class teamlead(akhiles,ankush):
    def show(self):
        print("dynamic website created",)



t=teamlead()
t.backend()
t.frontend()
t.show()
# class akhiles:
#     back = "oracle DB & java"
#     def backend(self):
#         print("backend task implemented using", self.back)
#
# class ankush:
#     front = "html css & js"
#     def frontend(self):
#         print("frontend task implemented using", self.front)
#
# class teamlead(akhiles, ankush):
#     def show(self):
#         print("dynamic website created using", self.back, "and", self.front)
#
# t = teamlead()
# t.backend()
# t.frontend()
# t.show()