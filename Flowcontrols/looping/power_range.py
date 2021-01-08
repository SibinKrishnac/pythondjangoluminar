num=int(input("enter power")) #3
low=int(input("enter lower limit")) #3
upper=int(input("enter upperlimit")) #27

for i in range(1,(upper+1)): #1 2 3
    if i**num in range(low,upper): #1**3  2**3=8  3**3
        print(i,end=",")
