class employee:
    def __init__(self,id,name,desig,exp,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary
    def __str__(self):
        return self.name
from functools import reduce
f=open("employeelist.txt", "r")
emplst=[]
dev_sal=[]
for lines in f:
    id,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplst.append(employee(id, name, desig, exp, int(salary)))

#============================ to print salary of developer
for emp in emplst:
    if emp.desig=="developer":
        dev_sal.append(emp.salary)
print(dev_sal)

#=============   to print highest and lowest sal using lambda
high=int(reduce(lambda no1,no2:no1 if no1>no2 else no2,dev_sal))
low=int(reduce(lambda no1,no2:no1 if no1<no2 else no2,dev_sal))
print("Highest salary:",high)
print("Lowest salary:",low)

