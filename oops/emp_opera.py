class employee:
    def __init__(self,id,name,desig,exp,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary
    def __str__(self):
        return self.name
f=open("employees.txt","r")
emplst=[]
salarylst=[]
for lines in f:
    id,name,desig,exp,salary=lines.rstrip("\n").split(",")
    obj=employee(id,name,desig,exp,salary)
    emplst.append(obj)
# for employee in emplst:
#     print(employee)
for employ in emplst:
    salarylst.append(employ.salary)
highsal=(max(salarylst))
for employ in emplst:
    if employ.salary==highsal:
        print(employ.name)
        