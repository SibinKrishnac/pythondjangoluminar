class parent:
    def m1(self):
        print("parent 1")
class child(parent):
    def m2(self):
        print("child")
class Subchild(child):
    def m3(self):
        print("subchild")
obj=Subchild()
obj.m3()
obj.m2()
obj.m1()

