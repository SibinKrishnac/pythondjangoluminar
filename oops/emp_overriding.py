class students:
    def __init__(self,id,name,course,total):
        self.id=id
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
obj=students(100,"sibin","django",150)
obj1=students(101,"sreeragkm","mean",150)
obj2=students(103,"sreeram","django",150)
slist=[]
slist.append(obj)
slist.append(obj1)
slist.append(obj2)
totalmark=0
# print(slist)
for stud in slist:
    # print(stud)
    if stud.course=="django":
        totalmark+=stud.total
        # print(stud.name)
print(totalmark)
