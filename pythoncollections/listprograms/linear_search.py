lst=[10,11,12,13,14,15]
# limit=int(input("enter limit"))
# lst=list()
# for i in range(0,limit):
#     number=input("enter number")
#     lst.append(number)
element=int(input("enter element"))
flag=0
cnt=0
for num in lst:
    if (element==num):
        flag+=1
        break
    else:
        pass
    cnt+=1
if flag==0:
    print(("not found"))
else:
    print("element found at",cnt)