# lst=[1,2,3,4]
# num=int(input("enter number"))
# for i in lst:
#     for j in lst:
#         if (i+j==num):
#             print(i,j)

lst=[1,2,3,5]
num=int(input("enter number")) #7
for i in range(0,len(lst)): #1
    for j in range(i+1,len(lst)): #2
        if(lst[i]+lst[j]==num): #
            print(lst[i],lst[j])

# lst=[1,2,3,4]
# low=0
# upp=len(lst)-1
# element=int(input("enter element"))
# while(low<upp):
#     tot=lst[low]+lst[upp]
#     if(element==tot):
#         print(lst[low],lst[upp])
#         break
#     else:
#         low+=1
