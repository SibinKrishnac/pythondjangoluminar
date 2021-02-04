class book(object):
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return book(self.pages+other.pages ) #100+200  300
    def __sub__(self, other):
        return book(self.pages - other.pages)
    def __mul__(self, other):
        return book(self.pages * other.pages)

    def __str__(self):
        return str(self.pages)
obj=book(100)
obj1=book(200)
obj2=book(300)
obj3=book(400)
# print(obj)
# print(obj1)
print(obj-obj1+obj2*obj3)