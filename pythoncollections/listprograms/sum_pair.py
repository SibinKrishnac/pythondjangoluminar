# lst=[1,2,3,4]
# num=int(input("enter number"))
# for i in lst:
#     for j in lst:
#         if (i+j==num):
#             print(i,j)

# lst=[1,2,3,5]
# num=int(input("enter number")) #7
# for i in range(0,len(lst)): #1
#     for j in range(i+1,len(lst)): #2
#         if(lst[i]+lst[j]==num): #
#             print(lst[i],lst[j])

lst=[1,2,3,5]
#    0     3
low=0
upp=len(lst)-1 #3                                    3
element=int(input("enter element"))                  #3
while(low<upp):     #0<3                1<3          0<3     0<2     0<1
    tot=lst[low]+lst[upp]   #1+4=5      2+4=6        1+5=6   1+3=4   1+2=3
    if(element==tot):     #6=6                                       3=3
        print(lst[low],lst[upp]) #2,4                                1,2
        break
    elif(element<tot):                          #   3<6      3<4
        upp-=1   #1                                 2         1
    elif(element>tot):                          #
        low+=1