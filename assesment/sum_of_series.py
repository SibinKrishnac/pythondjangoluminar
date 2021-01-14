num=input("enter number")
i=1
data=0
if(int(num)>9):
    print("enter a  value less than 9")
else:
    while(i<=int(num)): #1<=2         2<=2      3>2
        res=num*i       #2*1=2        2*2=22
        data+=int(res)  #data=0+2=2   =2+22=24
        i+=1            #i=2          i=3
    print(data)

