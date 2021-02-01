# f=open("covid_19_india.csv","r")
# dict={}
# for lines in f:
#     data=lines.rstrip("\n").split(",")
#     #print(data)
#     state=data[3].rstrip("***")
#     if (state=="Telengana"):
#         state="Telangana"
#     confirmed_case=int(data[8])
#     if(state not in dict):
#         dict[state]=(confirmed_case)
#     else:
#         dict[state] =confirmed_case
# for k,v in dict.items():
#     print(k,"====>",v)
# res=sorted(dict,key=dict.get,reverse=True)
# print(res[0])
#================================================
# f=open("covid_19_india.csv","r")
# dict={}
# for lines in f:
#     state=data[3]
#     confirmed_cases=int(data[8])
#
#     if state not in dict:
#         dict[state]=confirmed_cases
#     else:
#         dict[state]=confirmed_cases
# for k,v in dict.items():
#      print(k,"====>",v)
#
# def print_covid(**kwargs):
#     state=kwargs["state"]
#     if state in dict:
#         print(dict[8])
# print_covid(state="Kerala")
#==========================================

