# lst=[2,6,4]
# temp=list()
# lst0=lst[1]+lst[2]
# lst1=lst[0]+lst[2]
# lst2=lst[0]+lst[1]
# temp.append(lst0)
# temp.append(lst1)
# temp.append(lst2)
# print(temp)
#
#

lst=[2,3,4,5]
total=sum(lst)
output=list()
for num in lst:
    output.append(total-num)
print(output)