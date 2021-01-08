num1=int(input("enter num 1"))
num2=int(input("enter num 2"))
num3=int(input("enter num 3"))

if (num1>num2) & (num1>num3):
    print("num1 is highest")
elif(num2>num1) & (num2>num3):
    print("num2 is highest")
elif(num3>num1)& (num3>num2):
    print("num3 is highest")
else:
    #(num1 == num2) &(num1 == num3):
    print("all numbers are equal")