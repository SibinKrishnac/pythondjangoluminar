num=int(input("Enter number")) #123
res=0
while(num>0): #123>0 12>0 1>0
    digit=num%10 #123%10 12%10=2 1%10=1
    res=res+digit**3  #res=0+3**3=27
    num//=10 #123//10=12
print(res)
