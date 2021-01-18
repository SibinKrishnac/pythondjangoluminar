str=input("enetr string")
#print(len(str))
length=len(str)-1 #6
reverse=""
while(length>=0): #6>=0
    #print(str[length],end="")
    reverse=reverse+str[length]
    length-=1
print(reverse)