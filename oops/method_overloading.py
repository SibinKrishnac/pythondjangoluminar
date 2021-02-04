#same function name different no of arguments
class parent:
    def add(self):
        print("add")
    def add(self,num1,num2):
        print(num1+num2)
    def add(self,num1):
        print(num1)
obj=parent()
obj.add(1)
