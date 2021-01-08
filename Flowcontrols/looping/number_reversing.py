#num=int(input("enter number"))
#reverse=0
#while (num>0):
 #   temp=num%10
  #  reverse=reverse*10+temp
   # num=num//10
#print(reverse)


num=int(input("enter number"))
while(num>0):
    digit=num%10
    print(digit,end="")
    num=num//10