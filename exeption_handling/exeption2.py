lst=[10,20,30]
pos=int(input("enter position to print element"))
num1=int(input("Enter 1st item"))
num2=int(input("Enter 2nd item"))
try:
    res = num1 / num2
    print(res)
    print(lst[pos])
except Exception as e:
    print(e.args)
    # print("invalid position")

