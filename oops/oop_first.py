class person:
    def setperson(self,age,name): #(local variables)
        self.age=age
        self.name=name # instance variables= variables with self prepended
    def printperson(self):
        print("name=",self.name)
        print("age=",self.age)
obj=person()
obj.setperson(25,"ajay") #initializing instance variables
obj.printperson()
print(obj.age)

# obj1=person()
# obj1.setperson(26,"vijay")
# obj1.printperson()
