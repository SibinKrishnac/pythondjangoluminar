n=int(input(("enter power")))
low=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
for i in range(1,upper+1):
    if i**n in range (low,upper):
        print(i,end=",")