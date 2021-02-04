class employee:
    def set_employee(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary##accessing using instances variable
    def print_employee(self):
        print("Id =",self.id)
        print("Name =",self.name)
        print("Designation =",self.designation)
        print("Salary =",self.salary)
    def __str__(self):
        return self.name
obj=employee()
obj.set_employee(1001,"Emp1","Python developer",25000)
obj.print_employee()
# print(obj.name) #accessing using reference variable
print(obj)