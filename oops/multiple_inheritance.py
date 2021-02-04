class parent:
    def m1(self):
        print("parent 1")
class child():
    def m1(self):
        print("child")
class Subchild(parent,child):
    def m3(self):
        print("subchild")
obj=Subchild()
# obj.m3()
# obj.m2()
obj.m1()

