employees=[[10,"christy","dataanalyst",50000],
    [11,"jhon","ba",30000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",30000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000],
]
#==========lowest salary who is a developer
dsalary_list=[]
for emp in employees:
     if emp[2]=="developer":
         dsalary_list.append(emp[3])

low_sal=min(dsalary_list)
for emp in employees:
    if   (emp[3]==low_sal):
        print(emp)
#(emp[2]=="developer") &



# number_of_employees=len(employees)
# print("number of employees=",number_of_employees)
# #========
# total_amnt=0
# for emp in employees:
#     total_amnt+=emp[3]
# print("total amnt=",total_amnt)
# #=======count
# dev_cnt=0
# data_cnt=0
# ba_cnt=0
# for emp in employees:
#     if emp[2]=="dataanalyst":
#         data_cnt+=1
#     elif emp[2]=="developer":
#         dev_cnt+=1
#     elif emp[2]=="ba":
#         ba_cnt+=1
# print("data analyst=",dev_cnt)
# print("developer count=",data_cnt)
# print("ba count=",ba_cnt)
# #========maximum salary
# salary_list=[]
# for emp in employees:
#     salary_list.append(emp[3])
# high_salary=max(salary_list)
# print(high_salary)
# for emp in employees:
#     if emp[3]==high_salary:
#         print(emp)







