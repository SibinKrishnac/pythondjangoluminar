class employee:
    def __init__(self,id,name,desig):
        self.id=id
        self.name=name
        self.desig=desig

    def print_emp(self):
        print(self.id,self.name,self.desig)
obj=employee(1000,"emp1","supervisor")
obj.print_emp()