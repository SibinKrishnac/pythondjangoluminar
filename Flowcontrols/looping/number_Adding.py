#a = int(input("Input an integer : "))
#p = 0
#for i in range(1, a+1):
# p += int(str(a)*i)
#print(p)


num = int(input("Input an integer : "))
i=1
data=0
while(i<=int(num)):
 res=num*i
 data+=int(res)
 i+=1
 print(data)

