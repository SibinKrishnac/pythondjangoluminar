pattern="ABABBACEEEEEEE"
dict={}
for ch in pattern: #a,b,a
     if ch not in dict: #a if not in dict a:1
        dict[ch]=1 #a:1
     else:
        dict[ch]+=1
print(ch, "is the most occuring character")
# #========to print key value pair
# for key,value in dict.items():
#     print(key,",",value)
print(dict.get("E"))
# print(dict)
# data=sorted(dict,key=dict.get,reverse=True)
# print(data)