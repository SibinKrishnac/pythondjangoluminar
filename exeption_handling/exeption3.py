num1=int(input("n1"))
num2=int(input("n2"))
try:
    res=num1/num2
    print("res:",res)
except:
    num2=int(input("n2"))
    try:
        res = num1 / num2
        print("res:", res)
    except:
        num2 = int(input("n2"))
        res = num1 / num2
        print("res:", res)
finally:
    print('i have database operation')
    print("i have file operation")