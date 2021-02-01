student={}
f=open("stu_list.py","r")
for lines in f:
    #print(lines)
    id,name,total,course=lines.rstrip("\n").split(",")
    if id not in student:
        student[id]={"id":id,"name":name,"total":total,"course":course}
def print_student(**kwargs):
    id=kwargs["id"]
    if id in student:
        print(student[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(student[id][prop])
        else:
            pass
    else:
        print("no student with this id")
print_student(id="1000",prop="total")














# def print_student(**kwargs):
#     roll=kwargs["roll"]
#     if roll in student:
#         print(student[roll]["name"])
#         if "prop" in kwargs:
#             prop=kwargs["prop"]
#             print(student[roll][prop])
#         else:
#             pass
#     else:
#         print("no student ")
# print_student(roll=1000,prop="course")
