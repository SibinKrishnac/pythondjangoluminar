low=int(input("enter lower limit"))
upper=int(input("enter upperlimit"))
flag=0
for num in range(low,(upper+1)):
    for i in range(2,num):
        if(num%i==0):
            flag=flag+1
            break
        else:
            flag=0
    if(flag==0):
        print(num)