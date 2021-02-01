employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id":1001,"name":"tomy","salary":30000,"exp":2},
    1002:{"id":1002,"name":"thomas","salary":35000,"exp":2},
    1003:{"id":1003,"name":"dany","salary":40000,"exp":2},
    1004:{"id":1004,"name":"jack","salary":45000,"exp":2},
}
# if 1001 in employee:
#     print(employee[1001]["name"])
# else:print("does not exist")
#===================
# if 1003 in employee:
#     print(employee[1003]["salary"])
# else:print("does not exist")
#====================
# def print_employee(id=None):
#     if id in employee:
#         print(employee[id]["name"])
#     else:
#         print("does not exist")
# print_employee(id=1000)
#==========================================
# def print_employee(id=None,prop=None):
#     if id in employee:
#         print(employee[id][prop])
#     else:
#         print("no value")
# print_employee(id=1000,prop="salary")
#======================================fetching id
# def print_employee(**kwargs):
#     #print(kwargs)
#     id=kwargs["id"]
#     if id in employee:
#         print(employee[id]["name"])
# print_employee(id=1001)
#======================================1 prop
# def print_employee(**kwargs):
#     id=kwargs["id"]
#     if id in employee:
#         print(employee[id]["name"])
#         if "prop" in kwargs:
#             prop=kwargs["prop"]
#             print(employee[id][prop])
#         else:
#             pass
#     else:
#         print("no emp with this id")
# print_employee(id=1000,prop="exp")

#=============================2 prop
def print_employee(**kwargs):
    id=kwargs["id"]
    if id in employee:
        print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])
        else:
            pass
    else:
        print("no emp in this id")
print_employee(id=1000,prop="salary")
