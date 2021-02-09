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
dev_sal=[]
for lines in f:
    id,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplst.append(employee(id,name,desig,exp,int(salary)))


    #====to print employees as developer
# devlop=list(filter(lambda obj:obj.desig=="developer",emplst))
# for emp in devlop:
#     print(emp)
# cnt=len(devlop)
# print(cnt)

#============= to find max sal
# maxsal=max(list(map(lambda emp:emp.salary,emplst)))
# print(maxsal)

#========to print msximum salary
for employ in emplst:
    salarylst.append(employ.salary)
print(salarylst)
print(max(salarylst))

#========to print desig is a developer
for emp in emplst:
    if emp.desig=="developer":
        print("developer:",emp)
        
# ========to print low and high sal whose desig as a developer
for emp in emplst:
    if emp.desig=="developer":
        dev_sal.append(emp.salary)
print(dev_sal)
print("low sal for developr:", min(dev_sal))
print("high sal for develop:",max(dev_sal))

# highsal=(max(salarylst))
# for employ in emplst:
#     if employ.salary==highsal:
#         print(employ.name)
# # for employ in emplst:
# #     if employ.desig=="developer":
# #         print(min(salarylst))
